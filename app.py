import streamlit as st


name=st.text_input("Enter your name")

st.title("Take the input")

if st.button("Submit"):
  st.write(f"Print the name: {name}")
  
