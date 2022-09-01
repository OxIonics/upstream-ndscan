import dataclasses
from ..interfaces.annotations import (AnnotationInterface,
                                      ComputedCurveAnnotationInterface,
                                      LocationAnnotationInterface,
                                      AnnotationType)
from .. import interfaces

# INTERFACES TODO: this class not currently used...
@dataclasses.dataclass
class Annotation(AnnotationInterface):

    def get_item(self):
        return []

@dataclasses.dataclass
class ComputedCurveAnnotation(ComputedCurveAnnotationInterface):
    def get_item(self, channel_ref_to_series_idx, make_curve_item, series, param):
        from ndscan.plots import annotation_items  # TODO: fix circular import!

        function_name = self.function_name
        if not annotation_items.ComputedCurveItem.is_function_supported(function_name):
            raise ValueError(f"Unsupported function: {function_name}")

        associated_series_idx = max(
            channel_ref_to_series_idx(chan)
            for chan in self.associated_channels
        )

        x_limits = [param.min, param.max]
        curve = make_curve_item(associated_series_idx)
        vb = series[associated_series_idx].view_box

        item = annotation_items.ComputedCurveItem(function_name, self.data, vb, curve, x_limits)
        return item

@dataclasses.dataclass
class LocationAnnotation(LocationAnnotationInterface):
    def get_item(self, channel_ref_to_series_idx, make_curve_item, series, param):
        return []

            # if a.kind == "location":
            #     if set(a.coordinates.keys()) == set(["axis_0"]):
            #         associated_series_idx = max(
            #             channel_ref_to_series_idx(chan)
            #             for chan in a.parameters.get("associated_channels", [None]))

            #         color = FIT_COLORS[associated_series_idx % len(FIT_COLORS)]
            #         vb = self.series[associated_series_idx].view_box
            #         line = VLineItem(a.coordinates["axis_0"],
            #                          a.data.get("axis_0_error", None), vb, color,
            #                          self.x_data_to_display_scale, self.x_unit_suffix)
            #         self.annotation_items.append(line)
            #         continue

# if a.kind == "curve":
#     associated_series_idx = None
#     for series_idx, series in enumerate(self.series):
#         match_coords = set(["axis_0", "channel_" + series.data_name])
#         if set(a.coordinates.keys()) == match_coords:
#             associated_series_idx = series_idx
#             break
#     if associated_series_idx is not None:
#         curve = make_curve_item(associated_series_idx)
#         series = self.series[associated_series_idx]
#         vb = series.view_box
#         item = CurveItem(a.coordinates["axis_0"],
#                          a.coordinates["channel_" + series.data_name], vb,
#                          curve)
#         self.annotation_items.append(item)
#         continue

#     function_name = a.parameters.get("function_name", None)
#     if ComputedCurveItem.is_function_supported(function_name):
#         associated_series_idx = max(
#             channel_ref_to_series_idx(chan)
#             for chan in a.parameters.get("associated_channels", [None]))

#         x_limits = [self.x_param_spec.get(n, None) for n in ("min", "max")]
#         curve = make_curve_item(associated_series_idx)
#         vb = self.series[associated_series_idx].view_box
#         item = ComputedCurveItem(function_name, a.data, vb, curve, x_limits)
#         self.annotation_items.append(item)
#         continue

# Promoting casting to subtypes of dataclasses seems messy...or am I missing something?
def interface_to_analysis(interface):
    iface_desc = interface.to_dict()

    interface_type = iface_desc.pop("interface_type")
    if interface_type != interfaces.common.InterfaceType.ANNOTATION:
        raise ValueError(f"Invalid interface type: {interface_type}")

    if not "interface_subtype" in iface_desc:
        raise ValueError(
            f"Invalid annotation interface description (missing annotation subtype): {iface_desc}"
        )

    subtype = AnnotationType(iface_desc.pop("interface_subtype"))

    if subtype == AnnotationType.COMPUTED_CURVE:
        return ComputedCurveAnnotation(**iface_desc)
    elif subtype == AnnotationType.CUSTOM:
        return interface
    elif subtype == AnnotationType.LOCATION:
        return LocationAnnotation(**iface_desc)

    raise ValueError(f"Unrecognised annotation subtype: {subtype}")
