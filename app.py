from flask import Flask, render_template, jsonify

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/evaluation')
def get_evaluation():
    return jsonify(model_evaluation)

@app.route('/api/attributes')
def get_attributes():
    return jsonify(model_attributes)

if __name__ == '__main__':
    app.run(debug=True)
