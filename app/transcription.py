import whisper
import ffmpeg
import os

def transcribe_video(video_path):
    """
    Extracts audio from a video and transcribes it using Whisper.
    """
    # Define the audio path
    # audio_path = os.path.splitext(video_path)[0] + ".wav"
    audio_path = "uploads/video.mp4"

    # Extract audio using FFmpeg
    ffmpeg.input(video_path).output(audio_path, format="mp4").run(overwrite_output=True)

    # Load Whisper model (choose "tiny", "base", or "small" for speed)
    model = whisper.load_model("base")

    # Transcribe audio
    result = model.transcribe(audio_path)

    # Clean up the temporary audio file
    os.remove(audio_path)

    # Return the transcription
    return result["text"]