import dataclasses
import json
from . import analysis, annotations, common, parameters, results

def decode(data) -> common.Interface:
    if isinstance(data, dict):
        data_dict = data
    else:
        data_dict = json.loads(data)

    if not "interface_type" in data_dict:
        raise ValueError(f"Invalid interface schema (missing interface type): {data}")

    interface_type = common.InterfaceType(data_dict.pop("interface_type"))

    if interface_type == common.InterfaceType.ANALYSIS:
        cls = analysis.AnalysisInterface
    elif interface_type == common.InterfaceType.ANNOTATION:
        cls = annotations.AnnotationInterface
    elif interface_type == common.InterfaceType.PARAM:
        cls = parameters.ParamInterface
    elif interface_type == common.InterfaceType.RESULT:
        cls = result.ResultInterface
    else:
        raise ValueError(f"Unrecognised interface type: {interface_type}")

    return cls.from_dict(data_dict)

# TODO: make these into unit tests!
def test_encode_decode():
    # todo: loop through all classes and fill out fields automatically
    iface = parameters.IntParamInterface(
        fqn="fqn",
        description="description",
        is_scannable=True,
        default="0",
        param_min=100,
        param_max=0,
        param_unit=1,
        scale="scale"
    )
    desc = iface.encode()
    decoded = decode(desc)
    assert decoded == iface

@dataclasses.dataclass
class FooParameterInterface(parameters.ParamInterface):
    foo: str

class FooParameterExp(FooParameterInterface):
    pass

class FooParameterApplet(FooParameterInterface):
    def __post_init__(self):
        print("applet init...")

def test_custom_encode_decode():
    iface_cls = common.make_custom_interface(FooParameterInterface,
                                             FooParameterApplet
                                            )
    iface = iface_cls(fqn="fqn",
                      description="a custom interface!",
                      is_scannable=False,
                      default="default",
                      foo="foo!"
                     )

    desc = iface.encode()
    applet_iface = decode(desc)
if __name__ == "__main__":
    test_encode_decode()
    test_custom_encode_decode()


