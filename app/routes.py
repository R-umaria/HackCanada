from flask import Blueprint, render_template, request, jsonify
from app.utils import ask_gemini

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