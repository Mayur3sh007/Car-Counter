from ultralytics import YOLO
import cv2

# Load the PyTorch YOLO model
model = YOLO('yolov8s.pt')

# Export the model to openvino format
model.export(format = 'openvino')

# vinomodel = YOLO('Yolo-Weights/yolov8n_openvino_model')
# vinoresult = vinomodel('../Assets/images/School_Bus.jpg', show=True)
# cv2.waitKey(0)
