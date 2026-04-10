from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("http://message-api:5001/message", timeout=3)
        data = response.json()
        return f"Web-app received: {data['message']}"
    except Exception as e:
        return f"Error contacting message-api: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)