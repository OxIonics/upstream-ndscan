import enum
import dataclasses
from . import common

class AnalysisType(enum.Enum):
    pass

@dataclasses.dataclass
class AnalysisInterface(common.Interface):
    def __post_init__(self):
        self.interface_type = common.InterfaceType.ANALYSIS
