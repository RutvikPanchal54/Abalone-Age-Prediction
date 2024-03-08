# import joblib
# from flask import Flask, request, jsonify, render_template
# import numpy as np

# # Load the best machine learning model using joblib
# best_model = joblib.load('C:/Users/Rutvik Panchal/Desktop/Python/Bit/Model/Abalone Model/best_abalone_model.pkl')

# # Create a Flask web application
# app = Flask(__name__)

# # Route for rendering the home page
# @app.route('/')
# def home():
#     return render_template('home.html')

# # API route for making predictions (receives data in JSON format)
# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.json['data']
#     new_data = [list(data.values())]
#     output = best_model.predict(new_data)[0]
#     return jsonify(output)

# # Route for receiving form data and making predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extracting all features from the form
#     data = [int(request.form['sex']),
#             float(request.form['length']),
#             float(request.form['diameter']),
#             float(request.form['height']),
#             float(request.form['wholeWeight']),
#             float(request.form['shuckedWeight']),
#             float(request.form['visceraWeight']),
#             float(request.form['shellWeight'])
#             ]

#     final_features = [np.array(data)]
#     output = best_model.predict(final_features)[0]
#     return render_template('home.html', prediction_text="Predicted Age: {}".output)

# # Route for receiving form data and making predictions
# if __name__ == "__main__":
#     app.run(debug=True)

# import joblib
# from flask import Flask, request, jsonify, render_template
# import numpy as np  # Import the NumPy library

# # Load the best machine learning model using joblib
# best_model = joblib.load('C:/Users/Rutvik Panchal/Desktop/Python/Bit/Model/Abalone Model/best_abalone_model.pkl')

# # Create a Flask web application
# app = Flask(__name__)

# # Route for rendering the home page
# @app.route('/')
# def home():
#     return render_template('home.html')

# # Route for displaying result.html content
# @app.route('/result')
# def result():
#     # Assuming you want to display a default message if prediction_text is not defined
#     return render_template('result.html', prediction_text="No prediction available.")

# # Route for receiving form data and making predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extracting all features from the form
#     data = [int(request.form['sex']),
#             float(request.form['length']),
#             float(request.form['diameter']),
#             float(request.form['height']),
#             float(request.form['wholeWeight']),
#             float(request.form['shuckedWeight']),
#             float(request.form['visceraWeight']),
#             float(request.form['shellWeight'])
#             ]

#     final_features = [np.array(data)]
#     output = best_model.predict(final_features)[0]
    
#     return render_template('result.html', prediction_text="Predicted Age: {}".format(round(output)))

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)

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
