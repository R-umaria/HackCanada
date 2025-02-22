import moviepy.editor as mp
import speech_recognition as sr
import os

def transcribe_video(video_path):
    """
    Extracts audio from a video and transcribes it using Google Speech Recognition.
    """
    # Define the audio path
    audio_path = os.path.join("uploads", "audio.wav")

    try:
        # Load the video
        video = mp.VideoFileClip(video_path)

        # Extract the audio from the video
        audio_file = video.audio
        audio_file.write_audiofile(audio_path)

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        # Convert speech to text using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)

        # Clean up the temporary audio file
        # if os.path.exists(audio_path):
        #     os.remove(audio_path)

        # Return the transcription
        return text

    except Exception as e:
        # Handle errors (e.g., no speech detected, API issues)
        print(f"Error transcribing video: {e}")
        return None