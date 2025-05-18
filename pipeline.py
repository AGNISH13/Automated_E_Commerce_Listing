import streamlit as st
from crud import video, transcripts, keyframes, keyframe_classes,final_class
from poc_whisper.whisper import transcribe_audio_from_bytes  # Importing Whisper processing
from poc_katna.katna import extract_keyframes    # Importing Katna processing
from poc_filtering.filtering import filter_images  # Importing Filtering
from poc_yolo.yolo2 import detect_objects  # Importing YOLO detection
from poc_gemini.top_ids import identify_product  # Importing Gemini classification
from poc_blip.caption_matching_blip import blip_filter  # Importing BLIP captioning
from poc_gemini.description import generate_product_description  # Importing Gemini classification


class Pipeline:
    def __init__(self):
        self.video_path = None
        self.video_id = ""
        self.transcript = ""
        self.description = ""
        self.final_keyframes = []
        self.step = 0
        self.steps = {
            1: "Video Uploaded - Processing audio with Whisper",
            2: "Transcript created - Extracting keyframes using Katna",
            3: "Keyframes extracted - Applying profanity filter",
            4: "Profanity filter applied - Running YOLO object detection",
            5: "YOLO object detection completed - Identifying the product with Gemini",
            6: "Product identified - Selecting final keyframes with BLIP",
            7: "Final keyframes selected - Generating product description",
            8: "Product description generated - Pipeline completed",
            0: "reset..."
        }

        self.flag_transcript = False
        self.flag_final_keyframe = False
        self.flag_description = False
        # self.flag_penultimate = False
        # self.flag_end = False

    def setup(self, video_path: str = None):
        self.video_path = video_path

    def get_step(self):
        # get step from db
        return self.step, self.steps[self.step]

    def create_video_obj(self):
        videoobj = video()
        self.video_id = videoobj.create(video_link=self.video_path)

        # set stepper db
        self.step = 1
        return self.video_id

    def run_steps(self): # update with stepper
        # transcripts_list = []
        # for i, path in enumerate(self.video_paths):

        # video_path = self.video_path
        # video_id = self.video_id
        # Process audio with Whisper
        # print("Processing audio with Whisper...")
        if self.step == 1:
            self.transcript = transcribe_audio_from_bytes(self.video_path)  # return audio transcript -> string

            # Create a transcript object and store the transcript
            transcriptobj = transcripts()
            self.transcipt_id = transcriptobj.create(video_id=self.video_id, transcript=self.transcript)
            self.flag_transcript = True
            # self.end()
        # print(transcipt_id)
        # print(transcriptobj.get_transcripts(video_id=video_id)['response'])

        elif self.step == 2:
    
            # print("Extracting keyframes using Katna...")
            keyframe_bins = extract_keyframes(self.video_path)
            keyframeobj = keyframes()
            self.keyframes_id = keyframeobj.create(video_id=self.video_id,keyframes=keyframe_bins)
            # print(keyframes_id)
        
        elif self.step == 3:

            keyframe_r=[] # keyframeobj.get_all_keyframes(video_id=video_id)['response'] !FIX
            # print("Applying profanity filter...")
            for keyframe_collection in keyframeobj.get_all_keyframes(video_id=self.video_id)['response']:
                keyframe_r.append(keyframe_collection)
            # print(keyframe_r)
            filtered_keyframes = filter_images(keyframe_r)
            keyframeobj.update_keyframes(self.video_id, filtered_keyframes)
            # print(filtered_keyframes)# return filtered_keyframes -> list[base64] 
        
        elif self.step == 4:

            # store in database

            # print("Running YOLO object detection...")
            # detected_keyframes, class_ids = detect_objects(filtered_keyframes)
            class_ids = detect_objects(self.video_id, filtered_keyframes)
            classobj = keyframe_classes()
            for classid in class_ids:
                classobj.create(video_id=classid['video_id'],keyframe_id=classid['keyframe_id'],classes=classid['class'])
            # print(class_ids[-1])
        
        elif self.step == 5:

            # Selecting top product using Gemini
            # print("Identifying the product with Gemini...")
            classobj = keyframe_classes()
            class_ids = classobj.get_classes(video_id=self.video_id)['response']
            confirmed_ids = identify_product(transcript,class_ids)  # Example user input
            finalclassobj = final_class()
            finalclassobj.create(self.video_id,classes=confirmed_ids)
            # print(f"Confirmed Product IDs: {confirmed_ids}")
            # confirmed_ids = ["bottle"]

        elif self.step == 6:

            # Selecting final keyframes using BLIP
            # print("Selecting final keyframes with BLIP...")
        
            blip_frame_obj = keyframes()
            finalclassobj = final_class()
            selected_keyframes = blip_frame_obj.get_all_keyframes(self.video_id)["response"]
            confirmed_ids = finalclassobj.get_final_classes(video_id=self.video_id)['response']
            matched_keyframes = blip_filter(selected_keyframes, confirmed_ids)
            self.final_keyframes = matched_keyframes
            # print(f"No. of keyframes selected by BLIP:\n{len(matched_keyframes)}")
            self.flag_penultimate = True
        
        elif self.step == 7:

            # Generate the product description
            # print("Generating product description using Gemini...")
            transcriptobj = transcripts()
            transcript = transcriptobj.get_transcripts(video_id=self.video_id)['response']
            product_description = generate_product_description(transcript)

            # print(f"Product Description:\n{product_description}")

            self.description = product_description
            self.flag_description == True
            self.end()
        # self.step = 8
        elif self.step == -1:
            pass
        
        else:
            raise ValueError(f"step counter out of bounds - {self.step}")
    
    def auto_run(self):
        if self.step == 0:
            st.write("Pipeline has started")
            self.create_video_obj()
        if self.step!= -1:
            self.run_steps()
        if self.step!= -1:
            self.step += 1

    # def reset(self):
    #     self.step = 0
    #     self.video_path = None
    #     self.video_id = ""
    #     self.transcript = ""
    #     self.product_description = ""
    #     self.final_keyframes = []
    #     return self.step

    def reset(self):
        self.step = 0
        self.flag_transcript = False
        self.flag_final_keyframe = False
        self.flag_description = False
    
    def end(self):
        self.step = -1