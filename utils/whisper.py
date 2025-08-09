import os
import subprocess
import io
import whisper
import numpy as np
from pydub import AudioSegment
import torch

from utils.mp4_mp3_conversion import mp3_conversion


def transcribe_audio_from_bytes(video_data, model_size="small"):
    """
    Transcribe audio from byte data using Whisper's ASR model.

    Args:
        video_data : mp4 file
        model_size (str): The size of the Whisper model to use (e.g., "small", "medium", "large").
    
    Returns:
        str: The transcribed text from the audio.
    """
    # Convert the video data to mp3
    audio_byte_data = mp3_conversion(video_data)

    # Convert byte data to an audio segment using pydub
    audio = AudioSegment.from_file(io.BytesIO(audio_byte_data))

    # Convert the audio segment to numpy array (waveform)
    # Whisper expects a mono channel, so we'll ensure it's mono (1 channel)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)  # Whisper works best with 16kHz audio
    
    # Convert audio to numpy array (whisper expects a numpy array)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

    # Normalize audio to [-1, 1] range, as Whisper expects this format
    samples = samples / np.max(np.abs(samples))

    # Load the Whisper model
    model = whisper.load_model(model_size)

    # Convert the numpy array to a tensor (required by Whisper)
    audio_tensor = torch.tensor(samples).unsqueeze(0)  # Add batch dimension
    
    # Transcribe the audio
    result = model.transcribe(samples)
    
    # Return the transcribed text
    return result['text']



# Example: Using a file-like object (io.BytesIO)
# Replace with your own audio file as bytes (e.g., from a file or HTTP response)



# Example: Assume you have audio byte data (e.g., from an uploaded file or other source)
# This is just a placeholder for actual audio byte data
# audio_byte_data = b"your_audio_byte_data_here"  # Replace this with actual byte data

# Call the function to transcribe the audio byte data



# input_file = "/home/agnish_gg/amazon_listing_sam/test_videos/videoplayback_3.mp4"

# # Check if the input file exists
# if not os.path.exists(input_file):
#     print(f"Error: The file '{input_file}' does not exist. Please upload it.")
# else:

# def mp3_conversion(input_file, model_size="base"):
#     # Initialize a BytesIO buffer to hold the MP3 data
#     mp3_buffer = io.BytesIO()

#     try:
#         # Convert MP4 to MP3 and store the output in the buffer (instead of a file)
#         process = subprocess.Popen(
#             ['ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', '-f', 'mp3', '-'],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )

#         # Read the MP3 data from the stdout (subprocess.PIPE)
#         mp3_data, _ = process.communicate()

#         if process.returncode == 0:
#             # Store the MP3 data in the buffer
#             mp3_buffer.write(mp3_data)

#             # Reset buffer position to the start
#             mp3_buffer.seek(0)

#             print("Conversion successful! The MP3 data is stored in the variable.")
#         else:
#             print("Conversion failed. ffmpeg error occurred.")

#     except Exception as e:
#         print(f"An error occurred during conversion: {e}")

#     # Optionally, you can read the MP3 data from the buffer for further use:
#     # For example, to get the byte content:
#     mp3_byte_data = mp3_buffer.getvalue()
#     return mp3_byte_data

# # Print the transcribed text
#     print("Transcription:")
#     print(transcription)
#     transcription = generate_product_description(transcript=transcription)
#     print(transcription)
#     # with open(output_file, 'wb') as mp3_file:
#     #             mp3_file.write(mp3_buffer.getvalue())
#     # print(mp3_byte_data)
    # print(f"MP3 data length: {len(mp3_byte_data)} bytes.")