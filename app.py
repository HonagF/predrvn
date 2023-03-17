import streamlit as st
import sklearn
import pickle
import numpy as np

st.title('REVENUE PREDICTION')
temp = st.number_input('Input Temperature')
t = np.array(temp).reshape(-1,1)
model = pickle.load(open('ice_scream_revenue', "rb"))
rvn = model.predict(t)
if st.button('Predict'):
  st.write('Revenue Prediction')
  st.success(float(rvn))
