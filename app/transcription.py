import whisper
import ffmpeg
import os

def transcribe_video(video_path):
    """
    Extracts audio from a video and transcribes it using OpenAI Whisper.
    """
    # Define the audio path
    audio_path = os.path.join("uploads", "audio.wav")
    
    try:
        # Extract audio using FFmpeg
        ffmpeg.input(video_path).output(audio_path, format="wav").run(overwrite_output=True)
        
        # Load Whisper model (choose "tiny", "base", or "small" for speed)
        model = whisper.load_model("base")
        
        # Transcribe audio
        result = model.transcribe(audio_path)
        
        # Return the transcription
        return result["text"]
    
    except Exception as e:
        print(f"Error transcribing video: {e}")
        return None
