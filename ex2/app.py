import os, socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"Salut din {os.environ.get('APP_NAME')}! Container: {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)