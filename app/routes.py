from flask import request, jsonify
from app import app

@app.route('/api/predict', methods=['POST'])
def predict():
   
        data = request.get_json()
        if data:
            return jsonify({"received_data": data}), 200
        else:
            return jsonify({"error": "No data received"}), 400
  
@app.route('/')
def hello():
    return jsonify('hello')