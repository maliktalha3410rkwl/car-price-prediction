from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
with open("catboost_car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Columns
feature_columns = ['Make','Year','FuelType','Transmission','Engine','Drivetrain',
                   'Length','Width','Height','SeatingCapacity','FuelTankCapacity']

numeric_columns = ['Year','Engine','Length','Width','Height','SeatingCapacity','FuelTankCapacity']

# Categorical mappings
categorical_mappings = {
    "Make": {7: "Toyota", 8: "Honda", 18: "Ford"},
    "FuelType": {2: "Diesel", 5: "Petrol"},
    "Transmission": {1: "Automatic", 2: "Manual"},
    "Drivetrain": {1: "FWD", 2: "RWD"}
}

# Prepare dropdown options for template
categorical_options = {col: {v:k for k,v in mapping.items()} for col, mapping in categorical_mappings.items()}

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_price = None
    if request.method == "POST":
        input_data = []
        for col in feature_columns:
            value = request.form.get(col)
            if col in numeric_columns:
                input_data.append(float(value))
            else:
                # Convert user-selected name to integer code
                input_data.append(categorical_options[col][value])

        input_df = pd.DataFrame([input_data], columns=feature_columns)
        predicted_price = model.predict(input_df)[0]
        predicted_price = round(predicted_price, 2)

    return render_template("index.html",
                           predicted_price=predicted_price,
                           feature_columns=feature_columns,
                           categorical_options=categorical_options)

if __name__ == "__main__":
    app.run(debug=True)
