from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received webhook:", data)
    return jsonify({"status": "received", "data": data})

if __name__ == "__main__":
    app.run()


