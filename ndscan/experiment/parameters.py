"""Fragment-side parameter containers.
"""

# The ARTIQ compiler does not support templates or generics (neither in the sense
# of typing.Generic, nor any other), yet requires the inferred types/signatures
# of fields to match across all instances of a class. Hence, we have no option
# but to hang our heads in shame and manually instantiate the parameter handling
# machinery for all supported value types, in particular to handle cases where e.g.
# both an int and a float parameter is scanned at the same time.
import dataclasses
from artiq.language import *
from artiq.language import units
from typing import Any, Dict, Optional, Tuple, Type, Union
from ..utils import eval_param_default, GetDataset
from .. import interfaces


__all__ = ["FloatParam", "IntParam", "StringParam"]


class InvalidDefaultError(ValueError):
    """Raised when a default value is outside the specified range of valid parameter
    values."""
    pass


class ParamStore:
    """
    :param identity: ``(fqn, path_spec)`` pair representing the identity of this param
        store, i.e. the override/default value it was created for.
    :param value: The initial value.
    """
    def __init__(self, identity: Tuple[str, str], value):
        self.identity = identity

        # KLUDGE: To work around ARTIQ compiler type inference failing for empty lists,
        # we rebind the function to notify parameter handles of changes if there are
        # none registered.
        self._handles = []
        self._notify = self._do_nothing

        self._value = self.coerce(value)

    @host_only
    def register_handle(self, handle):
        self._handles.append(handle)
        self._notify = self._notify_handles

    @host_only
    def unregister_handle(self, handle):
        self._handles.remove(handle)

        if not self._handles:
            self._notify = self._do_nothing


class FloatParamStore(ParamStore):
    @portable
    def _notify_handles(self):
        for h in self._handles:
            h._changed_after_use = True

    @portable
    def _do_nothing(self):
        pass

    @portable
    def get_value(self) -> TFloat:
        return self._value

    @portable
    def set_value(self, value):
        new_value = self.coerce(value)
        if new_value == self._value:
            return
        self._value = new_value
        self._notify()

    @portable
    def coerce(self, value):
        return float(value)


class IntParamStore(ParamStore):
    @portable
    def _notify_handles(self):
        for h in self._handles:
            h._changed_after_use = True

    @portable
    def _do_nothing(self):
        pass

    @portable
    def get_value(self) -> TInt32:
        return self._value

    @portable
    def set_value(self, value):
        new_value = self.coerce(value)
        if new_value == self._value:
            return
        self._value = new_value
        self._notify()

    @portable
    def coerce(self, value):
        return int(value)


class StringParamStore(ParamStore):
    @portable
    def _notify_handles(self):
        for h in self._handles:
            h._changed_after_use = True

    @portable
    def _do_nothing(self):
        pass

    @portable
    def get_value(self) -> TStr:
        return self._value

    @portable
    def set_value(self, value):
        new_value = self.coerce(value)
        if new_value == self._value:
            return
        self._value = new_value
        self._notify()

    @portable
    def coerce(self, value):
        return str(value)


class ParamHandle:
    """
    Each instance of this class corresponds to exactly one attribute of a fragment that
    can be used to access the underlying parameter store.

    :param owner: The owning fragment.
    :param name: The name of the attribute in the owning fragment bound to this
        object.
    """
    def __init__(self, owner: Type["Fragment"], name: str):
        self.owner = owner
        self.name = name
        assert name.isidentifier(), ("ParamHandle name should be the identifier it is "
                                     "referred to as in the owning fragment.")

        self._store = None
        self._changed_after_use = True

    def set_store(self, store) -> None:
        if self._store:
            self._store.unregister_handle(self)
        store.register_handle(self)
        self._store = store
        self._changed_after_use = True

    @portable
    def _change_cb(self):
        # Once transform lambdas are supported, handle them here.
        self._changed_after_use = True

    @portable
    def changed_after_use(self) -> TBool:
        return self._changed_after_use


class FloatParamHandle(ParamHandle):
    @portable
    def get(self) -> TFloat:
        return self._store.get_value()

    @portable
    def use(self) -> TFloat:
        self._changed_after_use = False
        return self._store.get_value()


class IntParamHandle(ParamHandle):
    @portable
    def get(self) -> TInt32:
        return self._store.get_value()

    @portable
    def use(self) -> TInt32:
        self._changed_after_use = False
        return self._store.get_value()


class StringParamHandle(ParamHandle):
    @portable
    def get(self) -> TStr:
        return self._store.get_value()

    @portable
    def use(self) -> TStr:
        self._changed_after_use = False
        return self._store.get_value()


def resolve_numeric_scale(scale: Optional[float], unit: str) -> float:
    if scale is not None:
        return scale
    if unit == "":
        return 1
    try:
        return getattr(units, unit)
    except AttributeError:
        raise KeyError("Unit '{}' is unknown, you must specify "
                       "the scale manually".format(unit))

# @dataclasses.dataclass
class FloatParam(interfaces.parameters.FloatParamInterface):
    HandleType: ParamHandle = FloatParamHandle
    StoreType: ParamStore = FloatParamStore
    CompilerType = TFloat

    def __post_init__(self):
        super().__post_init__()
        self.scale = resolve_numeric_scale(self.scale, self.unit)
        self.step = self.step if self.step is not None else self.scale / 10.0

    def eval_default(self, get_dataset: GetDataset) -> float:
        if type(self.default) is str:
            return eval_param_default(self.default, get_dataset)
        return self.default

    def make_store(self, identity: Tuple[str, str], value: float) -> FloatParamStore:
        if self.min is not None and value < self.min:
            raise InvalidDefaultError("Value {} below minimum of {}".format(
                value, self.min))
        if self.max is not None and value > self.max:
            raise InvalidDefaultError("Value {} above maximum of {}".format(
                value, self.max))
        return FloatParamStore(identity, value)


# @dataclasses.dataclass
class IntParam(interfaces.parameters.IntParamInterface):
    HandleType: ParamHandle = IntParamHandle
    StoreType: ParamStore = IntParamStore
    CompilerType = TInt32

    def __post_init__(self):
        self.scale = resolve_numeric_scale(self.scale, self.unit)
        if self.scale != 1:
            raise NotImplementedError(
                "Non-unity scales not implemented for integer parameters")

    def eval_default(self, get_dataset: GetDataset) -> int:
        if type(self.default) is str:
            return eval_param_default(self.default, get_dataset)
        return self.default

    def make_store(self, identity: Tuple[str, str], value: int) -> IntParamStore:
        if self.min is not None and value < self.min:
            raise InvalidDefaultError("Value {} below minimum of {}".format(
                value, self.min))
        if self.max is not None and value > self.max:
            raise InvalidDefaultError("Value {} above maximum of {}".format(
                value, self.max))
        return IntParamStore(identity, value)

# @dataclasses.dataclass
class StringParam(interfaces.parameters.StringParamInterface):
    HandleType = StringParamHandle
    StoreType = StringParamStore
    CompilerType = TStr

    def eval_default(self, get_dataset: GetDataset) -> str:
        return eval_param_default(self.default, get_dataset)

    def make_store(self, identity: Tuple[str, str], value: str) -> StringParamStore:
        return StringParamStore(identity, value)
