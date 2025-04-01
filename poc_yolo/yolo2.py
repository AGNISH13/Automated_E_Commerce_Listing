from ultralytics import YOLO

from utils.image_conversion import base64_to_image

# Collect base64 string from database and use YOLOv11

def detect_objects1(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Expected input_list to be of type list")
    if not all(isinstance(item, str) for item in input_list):
        raise ValueError("All elements in input_list must be base64-encoded strings")
    
    images = [base64_to_image(item) for item in input_list]  # Decode each base64 string into an image
    # images = [base64_to_image(item.get("keyframe")) for item in input_list] 
    object_id = []

    model = YOLO('yolo11n.pt')

    detections = []
    for image in images:
        results = model(image)

        # Handle results if it's a list
        if isinstance(results, list):
            results = results[0]

        boxes = results.boxes.xywh
        confidences = results.boxes.conf
        class_ids = results.boxes.cls
        class_names = results.names

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
    # Call Database

    # return detections, object_id
    return object_id

def detect_objects(video_id,keyframes):
    # if not isinstance(keyframes, list):
    #     raise TypeError("Expected input_list to be of type list")
    # if not all(isinstance(item, str) for item in keyframes):
    #     raise ValueError("All elements in input_list must be base64-encoded strings")
    print(video_id)
    # images = [base64_to_image(item) for item in input_list]  # Decode each base64 string into an image
    # images = [base64_to_image(item.get("keyframe")) for item in input_list] 
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
    # Call Database
        
        classid.append({
            'video_id': video_id,
            'keyframe_id': keyframe['_id'],
            'class':object_id
        })
    # return detections, object_id
    return classid





# list_image = redis_client.lrange('161458108048027478483967608718511976537',0,-1)
# print(list_image[5])
# image_data = base64.b64decode(list_image[5])
# image = retrieve_image_from_redis(image_data)
# detect_objects_with_yolo(image=image)
# # detect_objects_with_yolo('/Users/anirbang/Downloads/Hyundai-Creta-180120241405.jpg')
# print(object_id)
# # for image_byte in list_image:
# #     print(image_byte)
# #     image = retrieve_image_from_redis(image_byte)
# #     detect_objects_with_yolo(image)