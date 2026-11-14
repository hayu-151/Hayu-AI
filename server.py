
from flask import Flask, request, jsonify

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

    greetings = {
        "om": "Hayu AI: Afaan Oromoo keessatti si gargaaruuf qophaa'e.",
        "en": "Hayu AI: I am ready to help you in English.",
        "zh": "Hayu AI：我准备好帮助你了。",
        "ar": "Hayu AI: أنا مستعد لمساعدتك باللغة العربية."
    }

    return jsonify({
        "reply": greetings.get(language, greetings["om"]) + " Ergaa kee: " + message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
