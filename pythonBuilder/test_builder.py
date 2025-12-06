import json
from builder import layout, visualization, encoding


def build_test1_spec():
    test1 = (
        visualization()
        .mark("bar")
        .add_encoding(
            encoding()
            .channel("x").field("x")
            .channel("y").field("y")
            .channel("color").field("grey")
        )
    )

    test1 = test1.visualization
    test1["encoding"] = test1["encoding"].encoding

    return test1

def build_test2_spec():
    
    test2 = layout().direction("vertical").gap("5px").add_child(
            visualization()
            .mark("line")
            .add_encoding(
                encoding()
                .channel("x").field("x")
                .channel("y").field("y")
                .channel("color").field("blue")
            )
        ).add_child(
            layout().direction("horizontal").gap("5px")
            .add_child(
                visualization()
                .mark("point")
                .add_encoding(
                    encoding()
                    .channel("x").field("x")
                    .channel("y").field("y")
                    .channel("color").field("green")
                )
            ).add_child(
                visualization()
                .mark("area")
                .add_encoding(
                    encoding()
                    .channel("x").field("x")
                    .channel("y").field("y")
                    .channel("color").field("purple")
                )
            )
        )
    test2 = test2.layout
    test2["children"][0] = test2["children"][0].visualization
    test2["children"][0]["encoding"] = test2["children"][0]["encoding"].encoding
    test2["children"][1] = test2["children"][1].layout
    test2["children"][1]["children"][0] = test2["children"][1]["children"][0].visualization
    test2["children"][1]["children"][0]["encoding"] = test2["children"][1]["children"][0]["encoding"].encoding
    test2["children"][1]["children"][1] = test2["children"][1]["children"][1].visualization
    test2["children"][1]["children"][1]["encoding"] = test2["children"][1]["children"][1]["encoding"].encoding

    return test2

def test_example1_matches_json():
    test1 = build_test1_spec()
    with open("schemaExamples/example1.json", "r") as f:
        example1 = json.load(f)
    assert test1 == example1


def test_example2_matches_json():
    test2 = build_test2_spec()
    with open("schemaExamples/example2.json", "r") as f:
        example2 = json.load(f)
    assert test2 == example2

