# 🌾 Crop Recommendation System using Machine Learning

This project is an **AI-powered web application** that recommends the best crop to cultivate based on soil and climate parameters using a trained **machine learning model**. It combines the power of **data science**, **Flask web development**, and **model deployment** into one compact solution.

---

## 📌 Overview

Farmers often face difficulty in selecting the right crop to grow based on their soil properties and climatic conditions. This system uses a machine learning model trained on real agricultural data to make intelligent crop recommendations using the following features:

- **Nitrogen (N)**  
- **Phosphorus (P)**  
- **Potassium (K)**  
- **Temperature (°C)**  
- **Humidity (%)**  
- **pH Level**  
- **Rainfall (mm)**  

---

## 🚀 Demo

🔗 Launch locally with:

```bash
python app.py
```

📍 Open in browser:  
**http://127.0.0.1:5000/**

---

## 🧠 ML Pipeline

| Step              | Tool Used               | Description |
|-------------------|-------------------------|-------------|
| Data Preprocessing | `pandas`, `sklearn`     | Handled missing values, scaled data using MinMax and StandardScaler |
| Feature Scaling    | `MinMaxScaler`, `StandardScaler` | Normalized features for uniform model behavior |
| Model              | `RandomForestClassifier` | Trained model to classify crop labels |
| Output             | Crop Name               | e.g. `Rice`, `Maize`, `Banana`, etc. |

📦 Model Files:
- `model.pkl` – trained classifier
- `standscaler.pkl` – standard scaler
- `minmaxscaler.pkl` – min-max scaler

---

## 📂 Project Structure

```
Crop-Recommendation/
│
├── app.py                  # Flask web application
├── notebook/
│   ├── Crop_Recommendation.ipynb  # Model development notebook
│   ├── model.pkl           # Saved trained model
│   ├── standscaler.pkl     # Standard scaler
│   └── minmaxscaler.pkl    # MinMax scaler
│
├── templates/
│   └── index.html          # Web frontend (form + result)
├── static/
│   └── crop.png            # Web image asset
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

---

## 🌐 Web Application UI

The UI allows users to input environmental data and returns the best crop to cultivate:

📸 Example input:
- N = 90
- P = 42
- K = 43
- Temperature = 26.5
- Humidity = 80
- pH = 6.5
- Rainfall = 200

🎯 Output:
> ✅ **"Rice is the best crop to be cultivated right there."**

---

## 🛠️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crop-recommendation
cd crop-recommendation
```

### 2. Create and Activate Virtual Environment

```bash
conda create -n crop-env python=3.11 -y
conda activate crop-env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Open browser and navigate to `http://127.0.0.1:5000/`

---

## 🔍 Requirements

Create a `requirements.txt` file with:

```txt
flask
numpy
pandas
matplotlib.pyplot
seaborn
scikit-learn
pickle
```

Generate manually with:
```bash
pip freeze > requirements.txt
```

---

## 🧪 Testing

Try values from known datasets to validate predictions. The app handles scaling and preprocessing before prediction. Ensure `model.pkl`, `minmaxscaler.pkl`, and `standscaler.pkl` are present in the correct path.

---

## 🌱 Supported Crops

```text
1. Rice           2. Maize         3. Jute        4. Cotton
5. Coconut        6. Papaya        7. Orange      8. Apple
9. Muskmelon     10. Watermelon   11. Grapes     12. Mango
13. Banana       14. Pomegranate  15. Lentil     16. Blackgram
17. Mungbean     18. Mothbeans    19. Pigeonpeas 20. Kidneybeans
21. Chickpea     22. Coffee
```

---

## 📊 Model Performance

You can add metrics from the notebook:

- Accuracy: 98.5%
- Precision: 98%
- Confusion Matrix and Feature Importance shown in notebook

---

## 👨‍💻 Author

**Aryan Kaisth**  
📧 aryankaisthpvt@example.com  
🔗 GitHub: [Aryan-Kaisth](https://github.com/Aryan-Kaisth)

---
