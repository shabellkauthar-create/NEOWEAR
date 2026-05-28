from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

readings = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.json

    entry = {
        "breathingRate": data.get("breathingRate", 0),
        "status": data.get("status", "UNKNOWN"),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    readings.insert(0, entry)

    if len(readings) > 20:
        readings.pop()

    return jsonify({"ok": True})


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(readings)


if __name__ == "__main__":
    app.run(debug=True)
