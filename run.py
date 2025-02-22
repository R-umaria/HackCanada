from app import create_app
import os

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = create_app()

# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# app.config["ALLOWED_EXTENSIONS"] = {"mp4", "avi", "mov"}

# def allowed_file(filename):
#     """Check if file has an allowed extension."""
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

if __name__ == "__main__":
    app.run(debug=True)
