import streamlit as st
import sklearn
import pickle

st.title('REVENUE PREDICTION')
temp = st.number_input('Input temperature')

model = pickle.load(open(ice_scream_revenue))
if st.button('Predict'):
  