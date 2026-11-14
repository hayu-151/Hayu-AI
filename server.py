import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://hayu-151.github.io"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route("/")
def home():
    return "Hayu AI Server is running!"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    language = data.get("language", "om")

    if not message:
        return jsonify({"reply": "Ergaa kee barreessi."}), 400

    if len(message) > 2000:
        return jsonify({"reply": "Ergaan kee dheeraa dha."}), 400

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"reply": "API key hin argamne."}), 500

    language_names = {
        "om": "Afaan Oromoo",
        "en": "English",
        "zh": "Chinese",
        "ar": "Arabic"
    }

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-6-luna",
            instructions=(
                "You are Hayu AI, a helpful and friendly assistant. "
                "Reply in " + language_names.get(language, "Afaan Oromoo") +
                ". Keep answers clear and useful."
            ),
            input=message
        )

        return jsonify({"reply": response.output_text})

    except Exception:
        app.logger.exception("OpenAI API request failed")
        return jsonify({
            "reply": "Dhiifama, yeroo ammaa deebii kennuu hin dandeenye."
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
