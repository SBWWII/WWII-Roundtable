import os
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))  # Uses Railway's assigned port if available, otherwise defaults to 5000

@app.route("/")
def home():
    return "Flask is running on Railway!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)