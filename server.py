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

    return jsonify({
        "reply": "Hayu AI ergaa kee fudhate: " + message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
