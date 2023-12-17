from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('iris_classifier.pkl')

nom = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}

@app.route('/')
def index():
    return render_template('template.html')
        
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.json
            prediction_num = model.predict([data['features']])[0]
            prediction_name = nom[prediction_num]
            return jsonify({'prediction': prediction_name})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
