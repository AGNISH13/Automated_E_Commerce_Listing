import subprocess
import io

def mp3_conversion(input_file):
    # Initialize a BytesIO buffer to hold the MP3 data
    mp3_buffer = io.BytesIO()
    print("Converting MP4 to MP3...")
    try:
        # Convert MP4 to MP3 and store the output in the buffer (instead of a file)
        process = subprocess.Popen(
            ['ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', '-f', 'mp3', '-'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Read the MP3 data from the stdout (subprocess.PIPE)
        mp3_data, _ = process.communicate()

        if process.returncode == 0:
            # Store the MP3 data in the buffer
            mp3_buffer.write(mp3_data)

            # Reset buffer position to the start
            mp3_buffer.seek(0)

            print("Conversion successful! The MP3 data is stored in the variable.")
        else:
            print("Conversion failed. ffmpeg error occurred.")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")

    # Optionally, you can read the MP3 data from the buffer for further use:
    # For example, to get the byte content:
    mp3_byte_data = mp3_buffer.getvalue()
    return mp3_byte_data