from flask import Flask
import threading, time, requests

app = Flask(__name__)

URL = "https://refactored-lamp-r46wqgw6vgv62pr9r-8000.app.github.dev/auth/postback/tunnel?tunnel=1"

def ping():
    while True:
        try:
            r = requests.get(URL, timeout=10)
            print(f"Pinged: {r.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(240)  # Every 4 mins

@app.route("/")
def home():
    return "24/7 Codespace Bot Running"

threading.Thread(target=ping, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)