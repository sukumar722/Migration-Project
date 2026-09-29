from flask import Flask, jsonify
import os

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    return jsonify(message="Hello from demo-app on EKS", version=VERSION)

@app.route("/health")
def health():
    return jsonify(status="ok")
