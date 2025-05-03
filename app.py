from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
try:
    with open('logistic_model_pipeline.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Sample model evaluation and attributes
model_evaluation = {
    'accuracy': 0.95,
    'precision': 0.93,
    'recall': 0.92,
    'f1_score': 0.925
}

model_attributes = {
    'name': 'Antibiotic Resistance Predictor',
    'version': '1.0',
    'description': 'A machine learning model to predict antibiotic resistance from genome data'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/evaluation')
def get_evaluation():
    return jsonify(model_evaluation)

@app.route('/api/attributes')
def get_attributes():
    return jsonify(model_attributes)

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
        
        # Convert features to numpy array
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        probability = model.predict_proba(features)
        
        # Show prediction options
        prediction_options = {
            0: 'Susceptible',
            1: 'Resistant'
        }
        
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability[0][1]),
            'interpretation': prediction_options.get(int(prediction[0]), 'Unknown')
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
