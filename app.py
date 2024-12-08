import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
from keras.models import load_model
import streamlit as st 



start = '2010-01-01'
end = '2019-12-31'

st.title('Stock Market Prediction')
user_input = st.text_input('Enter Stock Ticket','AAPL')
# Download the data
df = yf.download('user_input', start=start, end=end)

# Display the first few rows of the DataFrame
#print(df.head())

# Optionally save the data to a CSV file
#df.to_csv('AAPL_stock_data.csv')

#Describing the Data
st.subheader('Data from 2010 - 2019')
st.write(df.describe())