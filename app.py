from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Loads chatbot UI

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = f"You said: {user_message}"  # Replace this with AI logic
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
