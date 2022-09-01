import enum
import dataclasses
from typing import Dict, Optional, List
from . import common, parameters

class AnnotationType(enum.Enum):
    COMPUTED_CURVE = "computed_curve"
    CUSTOM = "custom"
    LOCATION = "location"

@dataclasses.dataclass
class AnnotationInterface(common.Interface):
    """ Annotations add content to result data plots to display fits, highlight points
    of interest in the dataset, etc.
    """
    data: Optional[Dict]# = None

    def __post_init__(self):
        self.interface_type = common.InterfaceType.ANNOTATION

    @staticmethod
    def from_dict(data) -> common.Interface:
        if not "interface_subtype" in data:
            raise ValueError(
                f"Invalid annotation interface description (missing annotation subtype): {data}"
            )

        subtype = AnnotationType(data.pop("interface_subtype"))

        if subtype == AnnotationType.COMPUTED_CURVE:
            return ComputedCurveAnnotationInteface(**data)
        elif subtype == AnnotationType.CUSTOM:
            return common.CustomInterface.from_dict(data)
        elif subtype == AnnotationType.LOCATION:
            return LocationAnnotationInteface(**data)

        raise ValueError(f"Unrecognised annotation subtype: {subtype}")

@dataclasses.dataclass
class ComputedCurveAnnotationInteface(AnnotationInterface):
    function_name: str
    associated_channels: str

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationType.COMPUTED_CURVE


@dataclasses.dataclass
class LocationAnnotationInteface(AnnotationInterface):
    associated_channels: List
    associated_channels: str
    coordinates: Optional[Dict]# = None

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationType.LOCATION
