import whisper
import ffmpeg
import os

# Define video and audio paths
video_path = "./video/sample.mp4"
audio_path = "./video/sample.wav"

# Extract audio using FFmpeg
ffmpeg.input(video_path).output(audio_path, format="wav").run(overwrite_output=True)

# Load Whisper model (choose "tiny", "base", or "small" for speed)
model = whisper.load_model("base")

# Transcribe audio
result = model.transcribe(audio_path)

# Print transcription
print("Transcription:\n", result["text"])
