from flask import Flask, request, jsonify
from limiter import is_allowed

app = Flask(__name__)

@app.route('/resource')
def resource():
    api_key = request.headers.get("X-API-Key")
    if not api_key:
        return jsonify({"error": "Missing API key"}), 400

    if is_allowed(api_key):
        return jsonify({"message": "Access granted"}), 200
    else:
        return jsonify({"error": "Rate limit exceeded"}), 429
