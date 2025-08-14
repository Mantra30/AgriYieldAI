from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load models
classifier_model = joblib.load('model/classifier_model.pkl')
regression_model = joblib.load('model/yield_model.pkl')
label_encoder = joblib.load('model/label_encoder.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        features = [float(x) for x in request.form.values()]
        data = np.array([features])

        # Predict crop and yield
        crop_pred = classifier_model.predict(data)
        yield_pred = regression_model.predict(data)

        crop_name = label_encoder.inverse_transform(crop_pred)[0]
        yield_value = yield_pred[0]

        return render_template('index.html', 
            prediction_text=f"🌾 Best Crop: {crop_name}", 
            yield_text=f"📈 Expected Yield: {yield_value:.2f} kg/hectare"
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
