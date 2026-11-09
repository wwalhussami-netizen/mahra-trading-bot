
import os
import requests
from flask import Flask

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

@app.route("/")
def home():
    return "Mahra Trading Bot is running!"

@app.route("/status")
def status():
    return {
        "bot": "Mahra",
        "status": "online",
        "markets": ["XAUUSD", "US100"],
        "timeframe": "5 minutes",
        "trading": "Signals only - No automatic trades"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
