from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)


@app.get("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.get("/healthz")
def health_check():
    return jsonify(status="ok")
