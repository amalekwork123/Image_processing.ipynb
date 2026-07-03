import streamlit as st

st.title("Take the input")
name=st.text_input("Enter your name")



if st.button("Submit"):
  st.write(f"Print the name: {name}")
  
