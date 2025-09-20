import streamlit as st
st.title("My Biodata")
st.header("Personal Information")
name=st.text_input("Full Name","Mohan Raj")
age=st.number_input("Age", min_value=1, max_value=100, value=25)
gender=st.selectbox("Gender",["Male", "Female", "Others"])
dob=st.data_input("Data of Birth")

st.header("Contact Information")
email=st.text_input("Email","mohan@example.com")
phone=st.text_input("Phone Number","+91-1234567891")
address=st.text_area("Address","123,Main Street,City,Country")

st.header("Education")
education=st.text_area("Education Background","B.sc")

