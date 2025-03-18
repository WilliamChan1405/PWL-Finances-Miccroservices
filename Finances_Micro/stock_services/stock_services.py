from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

@app.route("/lookup", methods=["GET"])
def lookup():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        response = requests.get(f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={API_KEY}")
        response.raise_for_status()
        quote = response.json()
        return jsonify({
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        })
    except requests.RequestException:
        return jsonify({"error": "Failed to retrieve stock data"}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
