from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the CSV file
df_flight = pd.read_csv('Train_set_flight.csv')

# Load the pre-trained model
model = joblib.load('Flight_Price_Prediction.pkl')

# Define LabelEncoders as they were during training
airline_encoder = LabelEncoder()
source_encoder = LabelEncoder()
destination_encoder = LabelEncoder()
route_encoder = LabelEncoder()
total_stops_encoder = LabelEncoder()
additional_info_encoder = LabelEncoder()

# Fit encoders with the original data
airline_encoder.fit(df_flight['Airline'])
source_encoder.fit(df_flight['Source'])
destination_encoder.fit(df_flight['Destination'])
route_encoder.fit(df_flight['Route'])
total_stops_encoder.fit(df_flight['Total_Stops'])
additional_info_encoder.fit(df_flight['Additional_Info'])

@app.route('/')
def index():
    # Extract unique values for dropdowns
    airlines = df_flight['Airline'].unique()
    sources = df_flight['Source'].unique()
    destinations = df_flight['Destination'].unique()
    routes = df_flight['Route'].unique()
    total_stops = df_flight['Total_Stops'].unique()
    additional_info = df_flight['Additional_Info'].unique()
    
    return render_template('index.html',
                           airlines=airlines,
                           sources=sources,
                           destinations=destinations,
                           routes=routes,
                           total_stops=total_stops,
                           additional_info=additional_info)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    data = {
        'Airline': request.form['airline'],
        'Date_of_Journey': request.form['date_of_journey'],
        'Source': request.form['source'],
        'Destination': request.form['destination'],
        'Route': request.form['route'],
        'Total_Stops': request.form['total_stops'],
        'Additional_Info': request.form['additional_info']
    }
    
    # Convert the form data to DataFrame
    df_input = pd.DataFrame([data])
    
    # Convert 'Date_of_Journey' to datetime
    df_input['Date_of_Journey'] = pd.to_datetime(df_input['Date_of_Journey'])
    
    # Convert 'Date_of_Journey' to a numeric feature (timestamp)
    df_input['Date_of_Journey'] = df_input['Date_of_Journey'].map(pd.Timestamp.toordinal)
    
    # Ensure columns are in the same order as training data
    feature_columns = ['Airline', 'Date_of_Journey', 'Source', 'Destination', 'Route', 'Total_Stops', 'Additional_Info']
    df_input = df_input[feature_columns]
    
    # Apply encoding to categorical features
    df_input['Airline'] = airline_encoder.transform(df_input['Airline'])
    df_input['Source'] = source_encoder.transform(df_input['Source'])
    df_input['Destination'] = destination_encoder.transform(df_input['Destination'])
    df_input['Route'] = route_encoder.transform(df_input['Route'])
    df_input['Total_Stops'] = total_stops_encoder.transform(df_input['Total_Stops'])
    df_input['Additional_Info'] = additional_info_encoder.transform(df_input['Additional_Info'])
    
    # Make prediction
    price = model.predict(df_input)[0]
    
    # Render the result with the predicted price
    return render_template('index.html',
                           airlines=df_flight['Airline'].unique(),
                           sources=df_flight['Source'].unique(),
                           destinations=df_flight['Destination'].unique(),
                           routes=df_flight['Route'].unique(),
                           total_stops=df_flight['Total_Stops'].unique(),
                           additional_info=df_flight['Additional_Info'].unique(),
                           price=round(price, 2))

if __name__ == '__main__':
    app.run(debug=True)
