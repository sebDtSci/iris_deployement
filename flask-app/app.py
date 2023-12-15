from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('iris_classifier.pkl')

@app.route('/')
def index():
    return render_template('template.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.json
            prediction = model.predict([data['features']])
            return jsonify({'prediction': int(prediction[0])})
        except:
            return jsonify({'error': 'Something went wrong!'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
