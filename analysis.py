import streamlit as st


file_bytes = st.file_uploader('Upload a file', type='csv')

If file_byte is not NONE:
  data = pd.read_csv(file_bytes)
