from ultralytics import YOLO

from utils.image_conversion import base64_to_image

# Collect base64 string from database and use YOLOv11

def detect_objects(video_id,keyframes):
    
    classid = []
    model = YOLO('yolo11n.pt')
    detections = []
    for keyframe in keyframes:
        image = base64_to_image(keyframe['keyframe'])
        results = model(image)

        # Handle results if it's a list
        if isinstance(results, list):
            results = results[0]

        boxes = results.boxes.xywh
        confidences = results.boxes.conf
        class_ids = results.boxes.cls
        class_names = results.names
        object_id = []
        for i in range(len(boxes)):
            # Extract the detection details
            x_center, y_center, width, height = boxes[i]
            confidence = confidences[i]
            class_id = int(class_ids[i])
            class_name = class_names[class_id]

            # Append the detection data
            detections.append({
                'class_id': class_id,
                'class_name': class_name,
                'confidence': confidence.item(),
                'x_center': x_center.item(),
                'y_center': y_center.item(),
                'width': width.item(),
                'height': height.item()
            })
            object_id.append({
                'class_id': class_id,
                'class_name': class_name
            })
        classid.append({
            'video_id': video_id,
            'keyframe_id': keyframe['_id'],
            'class':object_id
        })
    
    return classid