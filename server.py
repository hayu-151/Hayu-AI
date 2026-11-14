from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hayu AI Server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    return jsonify({
        "reply": "Hayu AI ergaa kee fudhate: " + message
    })

if __name__ == "__main__":
    app.run()