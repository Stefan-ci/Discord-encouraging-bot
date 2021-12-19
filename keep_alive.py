from flask import Flask
from threading import Thread, ThreadError

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I'm still alive. Thx !"

def run():
    app.run(host='0.0.0.0', port=8080, debug=False)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

