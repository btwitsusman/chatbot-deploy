from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello! This is your AI Chatbot."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = f"AI Response to: {user_input}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
