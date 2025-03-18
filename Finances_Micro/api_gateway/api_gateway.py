from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICES = {
    "auth": "http://localhost:5002",
    "stock": "http://localhost:5001"
}

@app.route("/<service>/<path:path>", methods=["GET", "POST"])
def proxy(service, path):
    if service in SERVICES:
        url = f"{SERVICES[service]}/{path}"
        if request.method == "GET":
            response = requests.get(url, params=request.args)
        else:
            response = requests.post(url, json=request.json)
        return jsonify(response.json())
    return jsonify({"error": "Service not found"}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)
