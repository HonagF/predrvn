import streamlit as st
import sklearn
import pickle

st.title('REVENUE PREDICTION')
temp = st.number_input('Input Temperature')
model = pickle.load(open('ice_scream_revenue', "rb"))
rvn = model.predict(temp)
if st.button('Predict'):
  st.success(rvn)
