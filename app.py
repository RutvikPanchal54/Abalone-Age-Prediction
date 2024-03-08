import joblib
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__, static_url_path='/static')

best_model = joblib.load('C:/Users/Rutvik Panchal/Desktop/Python/Bit/Model/Abalone Model/best_abalone_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template('result.html', prediction_text="No prediction available.")

@app.route('/predict', methods=['POST'])
def predict():
    data = [
        int(request.form['sex']),
        float(request.form['length']),
        float(request.form['diameter']),
        float(request.form['height']),
        float(request.form['wholeWeight']),
        float(request.form['shuckedWeight']),
        float(request.form['visceraWeight']),
        float(request.form['shellWeight'])
    ]

    final_features = [np.array(data)]
    output = best_model.predict(final_features)[0]

    return render_template('result.html', prediction_text="Predicted Age: {}".format(round(output)))

if __name__ == "__main__":
    app.run(debug=True)
