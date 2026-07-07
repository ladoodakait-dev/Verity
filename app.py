from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {"demo": {"tokens": 20}}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id", "demo")
    message = data.get("message", "")

    if users[user_id]["tokens"] <= 0:
        return jsonify({"error": "No tokens left. DM to buy more."}), 402
    
    users[user_id]["tokens"] -= 1
    reply = f"ChefBot: For '{message}', here are 4 steps: \n1. Heat oil\n2. Add spices\n3. Cook for 10 min\n4. Serve hot"
    
    return jsonify({"reply": reply, "tokens_left": users[user_id]["tokens"]})

@app.route("/")
def home():
    return "ChefBot API is Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
