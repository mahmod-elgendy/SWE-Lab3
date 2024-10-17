from flask import request, jsonify

TOKEN = "17102003"

def authenticationToken():
    token = request.headers.get("Authentication")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized token"}), 401