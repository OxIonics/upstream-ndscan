import enum
import dataclasses
from typing import Any, Dict, Optional, List
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

    def get_sources(self):
        return [self.data]

    @classmethod
    def from_dict(cls, data) -> common.Interface:
        if not "interface_subtype" in data:
            raise ValueError(
                f"Invalid annotation interface description (missing annotation subtype): {data}"
            )

        subtype = AnnotationType(data.pop("interface_subtype"))

        if subtype == AnnotationType.COMPUTED_CURVE:
            return ComputedCurveAnnotationInterface(**data)
        elif subtype == AnnotationType.CUSTOM:
            return common.CustomInterface.from_dict(data)
        elif subtype == AnnotationType.LOCATION:
            return LocationAnnotationInterface(**data)

        raise ValueError(f"Unrecognised annotation subtype: {subtype}")

@dataclasses.dataclass
class ComputedCurveAnnotationInterface(AnnotationInterface):
    function_name: str
    associated_channels: str

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationType.COMPUTED_CURVE


@dataclasses.dataclass
class LocationAnnotationInterface(AnnotationInterface):
    associated_channels: List
    associated_channels: str
    coordinates: Optional[Dict]# = None

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationType.LOCATION

    def get_sources(self):
        return super().get_sources() + [self.coordinates]

# TODO: CURVE Annotation

class AnnotationDataSourceType(enum.Enum):
    ANALYSIS_RESULT = "analysis_result"
    CUSTOM = "custom"
    FIXED = "fixed"
    ONLINE_RESULT = "online_result"

# Where should this live?
@dataclasses.dataclass
class AnnotationDataSourceInterface(common.Interface):
    def __post_init__(self):
        self.interface_type = common.InterfaceType.ANNOTATION_DATA_SOURCE

    @classmethod
    def from_dict(cls, data) -> common.Interface:
        if not "interface_subtype" in data:
            raise ValueError(
                f"Invalid annotation data source interface (missing subtype): {data}"
            )

        subtype = AnnotationDataSourceType(data.pop("interface_subtype"))

        if subtype == AnnotationDataSourceType.ANALYSIS_RESULT:
            return AnalysisResultSourceInterface(**data)
        elif subtype == AnnotationDataSourceType.CUSTOM:
            return common.CustomInterface.from_dict(data)
        elif subtype == AnnotationDataSourceType.FIXED:
            return FixedDataSourceInterface(**data)
        elif subtype == AnnotationDataSourceType.ONLINE_RESULT:
            return OnlineResultDataSourceInterface(**data)

        raise ValueError(f"Unrecognised annotation subtype: {subtype}")

@dataclasses.dataclass
class FixedDataSourceInterface(AnnotationDataSourceInterface):
    value: Any

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationDataSourceType.FIXED

@dataclasses.dataclass
class OnlineResultDataSourceInterface(AnnotationDataSourceInterface):
    analysis_name: Any  # TYPE?
    result_key: str

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationDataSourceType.ONLINE_RESULT

@dataclasses.dataclass
class AnalysisResultSourceInterface(AnnotationDataSourceInterface):
    name: str

    def __post_init__(self):
        super().__post_init__()
        self.interface_subtype = AnnotationDataSourceType.ANALYSIS_RESULT
