
from flask import Flask, request, jsonify
import re
import ast
import operator

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

def calculate(text):
    match = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([+*/-])\s*(-?\d+(?:\.\d+)?)\s*", text)
    if not match:
        return None

    a, op, b = match.groups()
    a, b = float(a), float(b)

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    if op == "/" and b == 0:
        return "Lakkoofsa zeeroon hiruun hin danda'amu."

    result = operations[op](a, b)
    return f"Deebiin isaa: {result:g}"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    language = data.get("language", "om")

    if not message:
        return jsonify({"reply": "Mee gaaffii kee barreessi."})

    text = message.lower().strip()
    reply = None

    if language == "en":
        if any(x in text for x in ["hello", "hi", "hey"]):
            reply = "Hello! I am Hayu AI. How can I help you?"
        elif "your name" in text:
            reply = "My name is Hayu AI."
        elif "thank" in text:
            reply = "You're welcome!"
        elif "help" in text or "study" in text:
            reply = "Of course! Tell me the subject or question you want help with."
        else:
            reply = "Please explain your question a little more."

    else:
        if "akkam" in text:
            reply = "Nagaa dha! Ati hoo akkam jirta?"
        elif "maqaan kee" in text:
            reply = "Maqaan koo Hayu AI dha. Maqaan kee eenyu?"
        elif text in ["hayu", "hayyu"]:
            reply = "Baga wal barree! Maal irratti si gargaaruu?"
        elif "galatoomi" in text:
            reply = "Maaloo! Si gargaaruun koo na gammachiisa."
        elif "barnoot" in text:
            reply = "Eeyyee! Herrega, Fiiziksii, Keemistirii, Baayoloojii fi Afaan Ingiliffaa irratti si gargaaruu nan danda'a. Gaaffii kee naaf ergi."
        elif "gargaarsa" in text or "gargaar" in text:
            reply = "Eeyyee! Maal irratti si gargaaruu?"
        elif "nagaa" in text:
            reply = "Nagaan koo gaarii dha. Ati hoo?"
        elif "eenyu" in text:
            reply = "Ani Hayu AI dha, gargaaraa dijitaalaa kee."
        else:
            answer = calculate(text)
            if answer is not None:
                reply = answer
            else:
                reply = "Gaaffii kee sirriitti naaf ibsi. Ani si gargaaruuf yaala."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
