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
    return "Hayu AI is running!"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip().lower()
    language = data.get("language", "om")

    if not message:
        reply = "Mee gaaffii kee barreessi."

    elif language == "en":
        if "hello" in message or "hi" in message:
            reply = "Hello! How can I help you today?"
        elif "your name" in message:
            reply = "My name is Hayu AI."
        elif "thank" in message:
            reply = "You're welcome!"
        else:
            reply = "I received your message. Please tell me more."

    else:
        if "akkam" in message:
            reply = "Nagaa dha! Ati hoo akkam jirta?"
        elif "maqaan kee" in message:
            reply = "Maqaan koo Hayu AI dha. Maqaan kee eenyu?"
        elif "galatoomi" in message:
            reply = "Maaloo! Si gargaaruun koo na gammachiisa."
        elif "eenyu" in message:
            reply = "Ani Hayu AI dha, gargaaraa dijitaalaa kee."
        elif "barnoota" in message or "barnootaa" in message:
    reply = "Eeyyee! Barnoota kee irratti si gargaaruu nan danda'a. Maal barachuu barbaadda? Herrega, Fiiziksii, Keemistirii, Baayoloojii moo Afaan Ingiliffaa?"

elif "barnoota" in message or "barnootaa" in message:
    reply = "Eeyyee! Barnoota kee irratti si gargaaruu nan danda'a. Maal barachuu barbaadda? Herrega, Fiiziksii, Keemistirii, Baayoloojii moo Afaan Ingiliffaa?"

elif "gargaarsa" in message:
    reply = "Eeyyee! Maal irratti si gargaaruu?"
        elif "nagaa" in message:
            reply = "Nagaan koo gaarii dha. Ati hoo?"
        else:
            reply = "Gaaffii kee naaf ibsi. Ani si gargaaruuf yaala."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
