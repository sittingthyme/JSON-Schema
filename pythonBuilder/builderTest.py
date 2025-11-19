import json
from builder import layout, visualization, encoding


test1 = visualization().mark("bar").add_encoding(encoding().channel("x").field("x").channel("y").field("y").channel("color").field("grey"))
test1 = test1.visualization
test1["encoding"] = test1["encoding"].encoding
with open("../schemaExamples/example1.json", "r") as f:
    example1 = json.load(f)

if test1 == example1:
    print("Example 1 is the same!")
else:
    print("Example 1 is not a match.")


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

with open("../schemaExamples/example2.json", "r") as f:
    example2 = json.load(f)

if test2 == example2:
    print("Example 2 is the same!")
else:
    print("Example 2 is not a match.")

