from crud import video, transcripts, keyframes, keyframe_classes,final_class
from utils.whisper import transcribe_audio_from_bytes  # Importing Whisper processing
from utils.katna import extract_keyframes    # Importing Katna processing
from utils.filtering import filter_images  # Importing Filtering
from utils.yolo2 import detect_objects  # Importing YOLO detection
from utils.top_ids import identify_product  # Importing Gemini classification
from utils.caption_matching_blip import blip_filter  # Importing BLIP captioning
from utils.description import generate_product_description  # Importing Gemini classification


def main():

    video_path = "/home/agnish_gg/Automated_E_Commerce_Listing-master/videoplayback_1.mp4"
    
    videoobj = video()
    video_id = videoobj.create(video_link=video_path)
    print(video_id)
    
    print("Processing audio with Whisper...")
    transcript = transcribe_audio_from_bytes(video_path)
    
    transcriptobj = transcripts()
    transcipt_id = transcriptobj.create(video_id=video_id,transcript=transcript)
    print(transcipt_id)
    print(transcriptobj.get_transcripts(video_id=video_id)['response'])

    print("Extracting keyframes using Katna...")
    keyframe_bins = extract_keyframes(video_path)
    keyframeobj = keyframes()
    keyframes_id = keyframeobj.create(video_id=video_id,keyframes=keyframe_bins)
    print(keyframes_id)
    
    print("Applying profanity filter...")
    keyframe_r=[]
    for keyframe_collection in keyframeobj.get_all_keyframes(video_id=video_id)['response']:
        keyframe_r.append(keyframe_collection)
    filtered_keyframes = filter_images(keyframe_r)
    keyframeobj.update_keyframes(video_id, filtered_keyframes)
    
    # store in database
    print("Running YOLO object detection...")
    class_ids = detect_objects(video_id,filtered_keyframes)
    classobj = keyframe_classes()
    for classid in class_ids:
        classobj.create(video_id=classid['video_id'],keyframe_id=classid['keyframe_id'],classes=classid['class'])
    print(class_ids[-1])
    
    # Selecting top product using Gemini
    print("Identifying the product with Gemini...")
    classobj = keyframe_classes()
    class_ids = classobj.get_classes(video_id=video_id)['response']
    confirmed_ids = identify_product(transcript,class_ids)
    finalclassobj = final_class()
    finalclassobj.create(video_id,classes=confirmed_ids)
    print(f"Confirmed Product IDs: {confirmed_ids}")

    # Selecting final keyframes using BLIP
    print("Selecting final keyframes with BLIP...")
    
    blip_frame_obj = keyframes()
    finalclassobj = final_class()
    selected_keyframes = blip_frame_obj.get_all_keyframes(video_id)["response"]
    confirmed_ids = finalclassobj.get_final_classes(video_id=video_id)['response']
    matched_keyframes = blip_filter(selected_keyframes, confirmed_ids)

    print(f"No. of keyframes selected by BLIP:\n{len(matched_keyframes)}")
    
    # Generate the product description
    print("Generating product description using Gemini...")
    transcriptobj = transcripts()
    transcript = transcriptobj.get_transcripts(video_id=video_id)['response']
    product_description = generate_product_description(transcript)

    print(f"Product Description:\n{product_description}")



if __name__ == "__main__":
    main()