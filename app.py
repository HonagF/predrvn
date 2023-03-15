import streamlit as st
import sklearn
import pickle

st.title('REVENUE PREDICTION')
temp = st.number_input('Input Temperature')
if st.button('Predict'):
  st.success('a')
