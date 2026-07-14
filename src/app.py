# app.py
from flask import Flask, request, jsonify
from predict import predict_visit

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON provided"}), 400

        if 'data' not in data:
            return jsonify({"error": "Expected 'data'"}), 400

        result = predict_visit(data['data'])

        return jsonify({
            "success": True,
            "prediction": result["prediction"],
            "probability": result["probability"]
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)