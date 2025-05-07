import streamlit as st
from crud import video, transcripts, keyframes, keyframe_classes,final_class
from poc_whisper.whisper import transcribe_audio_from_bytes  # Importing Whisper processing


class Pipeline:
    def __init__(self, video_paths):
        self.video_paths = video_paths
        self.video_ids = []

    def create_video_obj(self):
        video_id = []
        for file in self.video_paths:
            videoobj = video()
            video_id.append(videoobj.create(video_link=file))
        self.video_ids = video_id
        return video_id

    def run_pipeline(self): # update with stepper
        transcripts_list = []
        for i, path in enumerate(self.video_paths):
            # Process audio with Whisper
            print("Processing audio with Whisper...")
            transcript = transcribe_audio_from_bytes(path)  # return audio transcript -> string
            transcripts_list.append(transcript)

            # Create a transcript object and store the transcript
            transcriptobj = transcripts()
            transcipt_id = transcriptobj.create(video_id=self.video_ids[i], transcript=transcript)
            print(transcipt_id)
            print(transcriptobj.get_transcripts(video_id=self.video_ids[i])['response'])

            return transcripts_list