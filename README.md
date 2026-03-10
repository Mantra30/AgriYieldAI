# AgriYieldAI 🌾

AgriYieldAI is a machine learning based web application that predicts the **best crop to grow** and the **expected crop yield (kg/hectare)** based on soil and environmental conditions.

## 🚀 Features

* Predicts the **best crop** for given soil conditions.
* Estimates **crop yield (kg/hectare)**.
* Simple **web interface built with Flask**.
* Uses **Machine Learning models (Random Forest)** for predictions.

## 🧠 Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML

## 📊 Input Parameters

The model predicts results using the following inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

## ⚙️ How to Run the Project

1. Clone the repository

```
git clone <your-repo-link>
cd AgriYieldAI
```

2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Train the models

```
python model/model.py
```

5. Run the Flask application

```
python app.py
```

6. Open the application in your browser

```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
AgriYieldAI
│
├── model/
│   ├── model.py
│   ├── classifier_model.pkl
│   ├── yield_model.pkl
│   └── label_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
├── app.py
├── crop_data.csv
└── requirements.txt
```

## 🎯 Future Improvements

* Add real-time weather API
* Improve UI design
* Use larger agricultural datasets
* Deploy the app online

## 👨‍💻 Author

Mantra Hirani
