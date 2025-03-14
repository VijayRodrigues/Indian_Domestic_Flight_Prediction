
# ✈️ Indian Flight Price Prediction using Machine Learning  

🚀 **Predict flight ticket prices** for Indian domestic flights using a machine learning model trained with `HistGradientBoostingRegressor`. The project is deployed using a **Flask web application**, allowing users to input flight details and get real-time price predictions.

---

## 📌 Table of Contents  
- [📂 Project Structure](#-project-structure)  
- [🚀 Features](#-features)  
- [🔧 Installation & Setup](#-installation--setup)  
- [🎯 How It Works](#-how-it-works)  
- [📜 Technologies Used](#-technologies-used)  
- [📌 Screenshots](#-screenshots)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

---

## 📂 Project Structure  

![image](https://github.com/user-attachments/assets/70cf29b8-bf77-4b72-a48f-39f4a9cde9ec)



## 🚀 Features  

✅ Predicts flight prices based on **Airline, Source, Destination, Route, Stops, Date of Journey, Additional Info**  
✅ **Machine Learning Model:** Uses `HistGradientBoostingRegressor`  
✅ **Flask Web App:** User-friendly interface for predictions  
✅ **Dynamic Dropdowns:** Fetches unique flight details from dataset  
✅ **Data Preprocessing:** Converts categorical data using `LabelEncoder`  
✅ **Trained Model Stored:** Model saved as `Flight_Price_Prediction.pkl`  


📜 Technologies Used
✔️ Python
✔️ Flask
✔️ Scikit-Learn
✔️ Pandas & NumPy
✔️ HTML, CSS (For UI)


🎯 How It Works
**User Input:** The user provides flight details like **Airline, Source, Destination, Route, Stops, Date of Journey, Additional Info** via the web app.
**Data Preprocessing:**
🔹 Date is converted into a suitable format.
🔹 Categorical features are transformed using LabelEncoder.
**Prediction:**
🔹 The trained HistGradientBoostingRegressor model predicts the ticket price.
🔹 The model processes input features and outputs an estimated price.
**Result Display:**
🔹 The predicted price is displayed on the web interface.




🚀 Future Enhancements
🔹 Improve model accuracy using advanced ML techniques.
🔹 Deploy on cloud services like AWS/GCP/Azure.
🔹 Integrate live airline price APIs for better comparison.


Live Demo:
A live demo of the application is available at https://vrflightpred.pythonanywhere.com

