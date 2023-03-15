import streamlit as st
import sklearn
import pickle
import numpy as np

st.title('DU DOAN SO NAM DI TU CUA MAY')
temp = st.number_input('NHAP SO DA MAY CO (G)')
t = np.array(temp).reshape(-1,1)
model = pickle.load(open('ice_scream_revenue', "rb"))
rvn = model.predict(t)
if st.button('Predict'):
  st.write('MAY BI BO TU')
  st.success(float(rvn), ' NAM')
  st.write('NGU NHU CON CHO')
