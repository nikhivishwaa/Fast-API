from flask import Flask, jsonify

app = Flask("http://127.0.0.1:2000")

@app.route('/')
def index():
    return "hattp"