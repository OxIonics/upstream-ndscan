import numpy
import dataclasses
import enum
import importlib
import inspect
import json
from typing import Any, TypeVar

# TODO: find instances of "schema" / "schemata" in the code base and see which ones
# we can replace with more specific types / names
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        if isinstance(obj, numpy.floating):
            return float(obj)
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        if isinstance(obj, Interface):
            return obj.to_dict()
        if isinstance(obj, enum.Enum):
            return obj.value
        if hasattr(obj, "spec"):  # INTERFACES TODO AnnotationValueRef
            return obj.spec
        raise ValueError(f"Unsupported object type {obj}")

InterfaceType = TypeVar('T', bound='Parent')

class InterfaceType(enum.Enum):
    ANALYSIS = "analysis"
    ANNOTATION = "annotation"
    PARAM = "param"
    RESULT = "result"

@dataclasses.dataclass
class Interface():
    """ Base class for ndscan interfaces.

    Interfaces define the boundary between the experiment and applet sides of ndscan.
    They are convertible to and from string representations (see :meth encode: and
    :meth decode:), allowing them to be broadcast to applets as part of the scan
    metadata dataset and stored in experiments' HD5 files.

    Interfaces provide the subset of functionality which is shared between the
    experiment and applet side code. The specialised separately on the experiment/applet
    sides to add additional functionality which is only meaningful on one side.

    ndscan interfaces are extensible: users may define their own interface subtypes,
    which will be dynamically loaded on the applet side. See :class CustomInterface: for
    details.

    Attributes:
        interface_type: type of interface (see :class InterfaceType:)
    """

    interface_type: InterfaceType = dataclasses.field(init=False)
    interface_subtype: enum.Enum = dataclasses.field(init=False)

    def __post_init__(self):
        """ Implementations must set interface_type """
        raise NotImplementedError

    def encode(self):
        return json.dumps(self, cls=Encoder)

    @classmethod
    def from_dict(cls, data) -> InterfaceType:
        return cls(data)

    @staticmethod
    def get_type() -> enum.Enum:
        raise NotImplementedError

    def to_dict(self):
        return dataclasses.asdict(self)

def import_class(module_name: str, class_name: str) -> Any:
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        raise ValueError(f'Cannot import module "{module_name}"')

    module_classes = [
        name for name, obj in inspect.getmembers(module) if inspect.isclass(obj)
    ]

    if class_name not in module_classes:
        raise ValueError(f'Class "{class_name}" not in module "{module_name}"')

    cls = getattr(module, class_name)
    return cls

def make_custom_interface(interface_class: Interface, decodes_to: Optional[Interface]=None):
    """ Takes in an Interface class and returns a CustomInterface class. """
    decodes_to = decodes_to if decodes_to is not None else interface_class

    @dataclasses.dataclass
    class CustomInterfaceImpl(interface_class):

        applet_module: str = dataclasses.field(init=False)
        applet_class: str = dataclasses.field(init=False)

        def __post_init__(self):
            super().__post_init__()
            self.applet_module = applet_class.__module__
            self.applet_class = applet_class.__name__
            self.interface_subtype = interface_class.get_type().CUSTOM

        @classmethod
        def from_dict(data):
            applet_module = data.pop("applet_module")
            applet_class = data.pop("applet_class")
            return import_class(applet_module, applet_class)(**data)

    return CustomInterfaceImpl

class CustomInterface(Interface):
    applet_module: str = dataclasses.field(init=False)
    applet_class: str = dataclasses.field(init=False)

    @staticmethod
    def from_dict(data):
        applet_module = data.pop("applet_module")
        applet_class = data.pop("applet_class")
        return import_class(applet_module, applet_class)(**data)

