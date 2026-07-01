#streamlit run app.py
import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd

st.title("Car Price Prediction App")

pipe = pkl.load(open("pipe.pickle","rb"))
df = pd.read_csv("final_data.csv")

companies = sorted(df["company"].unique())
years = range(2000, 2027)

company = st.sidebar.selectbox("Select company", companies)

names = sorted(df[df["company"] == company]["name"].unique())

name = st.sidebar.selectbox("Select name", names)
year = st.sidebar.selectbox("Select year", years)
kms_driven = st.sidebar.number_input(
    "Enter km driven",
    value=50000,
    min_value=1000,
    max_value=200000
)

fuel = st.sidebar.selectbox(
    "Select fuel type",
    ["Petrol", "Disel"]
)

if st.sidebar.button("Predict Price"):

    st.write("You have selected:")
    st.write(f"Company: {company}")
    st.write(f"Name: {name}")
    st.write(f"Year: {year}")
    st.write(f"Kilometers Driven: {kms_driven}")
    st.write(f"Fuel Type: {fuel}")

    # check for user input
    myinput = [[company, name, year, kms_driven, fuel]]
    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']

    myinput = pd.DataFrame(data=myinput, columns=columns)

    result = pipe.predict(myinput)

    if result[0,0] < 0:
        st.write("Sorry, the predicted price is negative. Please check your input values.")
    else:
        st.write(f"Predicted Price is:", str(round(result[0,0])))
