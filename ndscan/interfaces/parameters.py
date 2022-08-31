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
    default: str

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
    param_min: float
    param_max: float
    param_unit: str  # CHECK type
    scale: float
    step: float

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.FLOAT

@dataclasses.dataclass
class IntParamInterface(ParamInterface):
    param_min: int
    param_max: int
    param_unit: str  # CHECK type
    scale: str  # CHECK type

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.INT

@dataclasses.dataclass
class StringParam(ParamInterface):
    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = ParamType.STR

