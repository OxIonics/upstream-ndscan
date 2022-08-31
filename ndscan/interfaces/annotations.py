import enum
import dataclasses
from typing import Dict
from . import common, parameters

class AnnotationType(enum.Enum):
    CUSTOM = "custom"

@dataclasses.dataclass
class AnnotationInterface(common.Interface):
#     parameters: Dict[str, parameters.ParamInterface]
#     coordinates: Dict[str, AnnotationDataSource]

    def __post_init__(self):
        self.interface_type = common.InterfaceType.ANNOTATION

#     @staticmethod
#     def from_dict(data) -> common.Interface:
#         if not "interface_subtype" in data:
#             raise ValueError(
#                 f"Invalid annotation interface schema (missing  annotation subtype): {data}"
#             )

#         self.parameters = {fqn: parameters.ParameterInterface.decode(desc) for fqn, desc in self.parameters.items()}

#         subtype = AnnotationType(data.pop("interface_subtype"))

#         if subtype == ParamType.CUSTOM:
#             return common.CustomInterface.from_dict(data)

#         raise ValueError(f"Unrecognised annotation subtype: {subtype}")

