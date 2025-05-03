from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample model evaluation and attributes
model_evaluation = {
    'accuracy': 0.95,
    'precision': 0.93,
    'recall': 0.92,
    'f1_score': 0.925
}

model_attributes = {
    'name': 'SampleModel',
    'version': '1.0',
    'description': 'A sample model for demonstration purposes'
}

@app.route('/model/evaluation', methods=['GET'])
def get_model_evaluation():
    return jsonify(model_evaluation)

@app.route('/model/attributes', methods=['GET'])
def get_model_attributes():
    return jsonify(model_attributes)

if __name__ == '__main__':
    app.run(debug=True)
