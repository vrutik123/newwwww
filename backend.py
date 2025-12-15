from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # VERY IMPORTANT for GitHub Pages

VALID_ID = "1234"
VALID_PASSWORD = "Ddu@2025"

@app.route("/login", methods=["POST"])
def login():
    student_id = request.form.get("student-id")
    password = request.form.get("password")

    if student_id == VALID_ID and password == VALID_PASSWORD:
        return "success", 200
    else:
        return "invalid", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
