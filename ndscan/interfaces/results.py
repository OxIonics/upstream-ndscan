import enum
import dataclasses
from . import common

class ResultType(enum.Enum):
    pass

@dataclasses.dataclass
class ResultInterface(common.Interface):
    def __post_init__(self):
        self.interface_type = common.InterfaceType.RESULT
