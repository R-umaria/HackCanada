from deepface import DeepFace

EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def detect_emotion(frame):
    """
    Detects the dominant emotion in a frame using DeepFace.
    """
    try:
        # Analyze the frame for emotions
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        # Extract the dominant emotion
        dominant_emotion = result[0]['dominant_emotion']
        return dominant_emotion
    except Exception as e:
        print(f"Error in emotion detection: {e}")
        return None
