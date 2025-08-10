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