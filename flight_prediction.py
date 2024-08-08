import pandas as pd
import numpy as np
import pickle


df_flight = pd.read_csv('Train_set_flight.csv')

def change_into_datetime(df, col, date_format=None, dayfirst=False):
    if date_format:
        df[col] = pd.to_datetime(df[col], format=date_format, errors='coerce')
    else:
        df[col] = pd.to_datetime(df[col], dayfirst=dayfirst, errors='coerce')
        

    
formats = {
    'Date_of_Journey': '%d/%m/%Y'
}

for col in formats:
    change_into_datetime(df_flight, col, date_format=formats[col])
    
    

from sklearn.preprocessing import LabelEncoder

LabelEncoder_y = LabelEncoder()
df_flight['Airline'] = LabelEncoder_y.fit_transform(df_flight['Airline'])
df_flight['Date_of_Journey'] = LabelEncoder_y.fit_transform(df_flight['Date_of_Journey'])
df_flight['Source'] = LabelEncoder_y.fit_transform(df_flight['Source'])
df_flight['Destination'] = LabelEncoder_y.fit_transform(df_flight['Destination'])
df_flight['Route'] = LabelEncoder_y.fit_transform(df_flight['Route'])
df_flight['Total_Stops'] = LabelEncoder_y.fit_transform(df_flight['Total_Stops'])
df_flight['Additional_Info'] = LabelEncoder_y.fit_transform(df_flight['Additional_Info'])


X = df_flight.drop(['Price'], axis = 1)
y = df_flight['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)


from sklearn.ensemble import HistGradientBoostingRegressor
grid_reg = HistGradientBoostingRegressor()
grid_reg.fit(X_train,y_train)


pickle.dump(grid_reg , open('Flight_Price_Prediction.pkl', 'wb'))