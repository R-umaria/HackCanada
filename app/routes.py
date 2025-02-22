from flask import Blueprint, render_template, request, jsonify
from app.utils import ask_gemini
from app.emotion_recognition import detect_emotion
import cv2
from collections import Counter

main = Blueprint("main", __name__)

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
    video_path = "uploads/video.mp4"
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

    # Return the count of detected emotions
    return jsonify(Counter(emotions))