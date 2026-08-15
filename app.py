from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mary_reyes_program_redesigned.html")
    return send_file(file_path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
