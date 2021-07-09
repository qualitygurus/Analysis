import streamlit as st
import pandas as pd


 
uploaded_file = st.file_uploader("Upload Files",type=['csv'])
if uploaded_file is not None:
 data = pd.read_csv(uploaded_file)
 st.write(data)
