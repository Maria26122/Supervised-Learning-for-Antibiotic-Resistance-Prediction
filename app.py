from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Placeholder for model prediction logic
def predict_resistance(genome_data):
    # This function should contain the logic to predict resistance or sensitivity
    # For demonstration, it returns a dummy response
    return {
        'genome': genome_data,
        'prediction': 'resistant' if len(genome_data) % 2 == 0 else 'sensitive'
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    genome_data = request.form.get('genome_data')
    if not genome_data:
        return jsonify({'error': 'No genome data provided'}), 400
    
    prediction_result = predict_resistance(genome_data)
    return jsonify(prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
