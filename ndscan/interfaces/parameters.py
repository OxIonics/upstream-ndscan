import enum
import dataclasses
from . import common

class ParamType(enum.Enum):
    FLOAT = "float_param"
    INT = "int_param"
    STR = "str_param"
    CUSTOM = "custom_param"

@dataclasses.dataclass
class ParamInterface(common.Interface):
    interface_subtype: ParamType = dataclasses.field(init=False)

    fqn: str
    description: str
    is_scannable: bool

    def __post_init__(self):
        self.interface_type = common.InterfaceType.PARAM

    @staticmethod
    def from_dict(data) -> common.Interface:
        if not "interface_subtype" in data:
            raise ValueError(
                f"Invalid parameter interface schema (missing parameter type): {data}"
            )

        subtype = ParamType(data.pop("interface_subtype"))

        if subtype == ParamType.FLOAT:
            return FloatParamInterface(**data)
        elif subtype == ParamType.INT:
            return IntParamInterface(**data)
        elif subtype == ParamType.STR:
            return StrParamInterface(**data)
        elif subtype == ParamType.CUSTOM:
            return common.CustomInterface.from_dict(data)

        raise ValueError(f"Unrecognised parameter type: {subtype}")

    @staticmethod
    def get_type() -> enum.Enum:
        return ParamType

@dataclasses.dataclass
class FloatParamInterface(ParamInterface):
    default: Union[str, float]
    min: Optional[float] = dataclasses.field(default=None, kw_only=True)
    max: Optional[float] = dataclasses.field(default=None, kw_only=True)
    unit: str = dataclasses.field(default="", kw_only=True)
    scale: Optional[float] = dataclasses.field(default=None, kw_only=True)
    step: Optional[float] = dataclasses.field(default=None, kw_only=True)

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.FLOAT

@dataclasses.dataclass
class IntParamInterface(ParamInterface):
    default: Union[str, int]
    min: Optional[int] = dataclasses.field(default=None, kw_only=True)
    max: Optional[int] = dataclasses.field(default=None, kw_only=True)
    unit: str = dataclasses.field(default="", kw_only=True)
    scale: Optional[int] = dataclasses.field(default=None, kw_only=True)

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.INT

@dataclasses.dataclass
class StringParam(ParamInterface):
    default: str

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.STR

