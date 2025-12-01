# 🚗 Car Price Prediction Web App

This repository contains a **Flask-based machine learning web application** that predicts car prices using a pre-trained **CatBoost regression model**.  
Users can input car features such as make, year, engine, fuel type, and dimensions, and the system outputs an estimated car price.

---

## 📌 Features

- Predicts car price using a CatBoost ML model  
- Clean and modern UI  
- Dropdowns for categorical features  
- Numeric inputs for car specifications  
- Flask-based backend for processing and prediction  
- Fully responsive design with HTML & CSS  

---

## 🧠 Technologies Used

- **Python 3**
- **Flask**
- **Pandas**
- **CatBoost Model (Pickle)**
- **HTML / CSS**

---

## 📂 Project Structure

car-price-prediction/
│
├── app.py
├── catboost_car_price_model.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md

---

## ⚙️ How the App Works

### ➤ Input Features

The model uses the following 11 features:

- Make  
- Year  
- FuelType  
- Transmission  
- Engine  
- Drivetrain  
- Length  
- Width  
- Height  
- SeatingCapacity  
- FuelTankCapacity  

### ➤ Categorical Mappings

The app internally converts selected text labels into numeric codes:

| Feature        | Options (User Input)        |
|----------------|-----------------------------|
| Make           | Toyota, Honda, Ford         |
| FuelType       | Diesel, Petrol              |
| Transmission   | Automatic, Manual           |
| Drivetrain     | FWD, RWD                    |

These values are mapped to encoded integers before prediction.

### ➤ Prediction Flow

1. User fills out form  
2. Flask reads input and converts categorical values  
3. Creates a DataFrame  
4. Passes it to the CatBoost model  
5. Predicts price  
6. Displays the result on the webpage  

---

