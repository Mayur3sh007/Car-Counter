from xml.etree.ElementTree import parse

tree = parse('../Yolo-Weights/yolov8n_openvino_model/yolov8n.xml')
root = tree.getroot()

# Find all layers in the XML
layers = root.findall('.//layer')

# Search for layers that might be input layers
input_layer_names = []
for layer in layers:
    layer_name = layer.attrib.get('name')
    # Check if the layer name contains common keywords like "images" or "input"
    if 'images' in layer_name.lower() or 'input' in layer_name.lower():
        input_layer_names.append(layer_name)

# Print the identified input layer names
if input_layer_names:
    print("Input layer(s) found:")
    for name in input_layer_names:
        print(name)
else:
    print("No input layer found in the XML.")
