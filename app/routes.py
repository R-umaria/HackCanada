from flask import Blueprint, render_template, request, jsonify
from app.utils import ask_gemini
from app.emotion_recognition import detect_emotion
from app.transcription import transcribe_video
import cv2
from collections import Counter
import os

main = Blueprint("main", __name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main.route("/")
def home():
    return render_template("index.html", title="Home")

@main.route("/ask-gemini", methods=["POST"])
def gemini_api():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    response = ask_gemini(prompt)
    return jsonify({"response": response})

@main.route('/analyze_video', methods=['POST'])
def analyze_video():
    """
    Endpoint to analyze a video for emotions.
    """
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    # Save the uploaded video file temporarily
    video_file = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, "recording.mp4")  # Consistent file name
    video_file.save(video_path)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    emotions = []

    # Set the frame skip interval (e.g., process 1 frame every 5 frames)
    frame_skip_interval = 5
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Skip frames based on the interval
        frame_count += 1
        if frame_count % frame_skip_interval != 0:
            continue

        # Detect emotion in the current frame
        emotion = detect_emotion(frame)
        if emotion:
            emotions.append(emotion)

    cap.release()

    # Clean up the temporary video file
    if os.path.exists(video_path):
        os.remove(video_path)

    # Return the count of detected emotions
    return jsonify(Counter(emotions))

@main.route('/transcribe_video', methods=['POST'])
def transcribe_video_endpoint():
    """
    Endpoint to transcribe a video using Whisper.
    """
    if 'video' not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    # Ensure the uploads directory exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Save the uploaded video file temporarily
    video_file = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, "recording.mp4")  # Consistent file name

    try:
        # Save the video file
        video_file.save(video_path)
        print(f"Video saved successfully at: {video_path}")

        # Transcribe the video
        transcription = transcribe_video(video_path)
        print(f"Transcription: {transcription}")

        # Return the transcription
        return jsonify({"transcription": transcription})

    except Exception as e:
        print(f"Error during transcription: {e}")
        return jsonify({"error": f"Error transcribing video: {str(e)}"}), 500

