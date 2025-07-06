from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from executables.main_executale import exectute
from utils.log import logReport
import os

app = Flask(__name__)
CORS(app)

@app.route("/target", methods=["POST"])
def targetCollector():
    data = request.get_json()  

    if not data or "target" not in data:
        return jsonify({"detail": "Target not found in request"}), 400

    target = data["target"]
    logReport(f"[✓] Target received: {target}")
    print(f"[✓] Target received: {target}")
    exectute(target)

    return jsonify({"status": "started", "target": target}), 200



@app.route("/api/logs")
def log():
    log_file = os.path.join("db", "log_file.txt")
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            logs = f.read()
        return Response(logs, mimetype="text/plain")
    except Exception as e:
        return f"Error reading log: {e}", 500