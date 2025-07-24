from flask import Flask, request, render_template
import numpy as np
import pickle

# Load ML objects
model = pickle.load(open('notebook/model.pkl', 'rb'))
sc = pickle.load(open('notebook/standscaler.pkl', 'rb'))
mx = pickle.load(open('notebook/minmaxscaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get and convert form data
        N = float(request.form.get('Nitrogen'))
        P = float(request.form.get('Phosporus'))
        K = float(request.form.get('Potassium'))
        temp = float(request.form.get('Temperature'))
        humidity = float(request.form.get('Humidity'))
        ph = float(request.form.get('pH'))
        rainfall = float(request.form.get('Rainfall'))

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)
        prediction = model.predict(sc_mx_features)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction[0], None)
        if crop:
            result = f"{crop} is the best crop to be cultivated right there."
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    except Exception as e:
        result = f"Error during prediction: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
