import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("Social_Network_Ads.pkl","rb"))

st.title("Social Network Ads Prediction")

age = st.number_input("Enter Age",18)
salary = st.number_input("Enter Estimated Salary",10000)

features = np.array([[age, salary]])

group = model.predict(features)

st.write(f"Hello, *World!* :sunglasses: . Customer Group {group}")

