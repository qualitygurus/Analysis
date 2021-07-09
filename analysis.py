import streamlit as st


file_bytes = st.file_uploader('Upload a file', type='csv')

data = pd.read_csv(file_bytes)
st.write(data)
