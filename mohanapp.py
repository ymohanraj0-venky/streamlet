import streamlit as st
import datetime ad dt

# Page title
st.title("📄 My Biodata")

# Section: Personal Info
st.header("👤 Personal Information")
name = st.text_input("Full Name", "Mohan Raj")
age = st.number_input("Age", min_value=1, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
dob = st.date_input("Date of Birth")
# Minimum age = 10 years
max_date = timedelta(days=365*10)

# Date of Birth (Calendar with restriction)
dob = st.date_input(
    "Date of Birth (Must be 10+ years old)",
    max_value=max_date
)

# Section: Contact Info
st.header("📞 Contact Information")
email = st.text_input("Email", "mohan@example.com")
phone = st.text_input("Phone Number", "+91-9876543210")
address = st.text_area("Address", "123, Main Street, City, Country")

# Section: Education
st.header("🎓 Education")
education = st.text_area("Educational Background","Bca")

# Section: Skills
st.header("💡 Skills")
skills = st.multiselect("Select Skills", 
                        ["Python", "Machine Learning", "Data Analysis", "Web Development", "Communication"],
                        default=["Python"])
st.header("📝 Biodata Summary")
if st.button("Generate Biodata"):
    st.subheader("Here’s Your Biodata:")
    st.write(f"*Name:* {name}")
    st.write(f"*Age:* {age}")
    st.write(f"*Gender:* {gender}")
    st.write(f"*Date of Birth:* {dob}")
    st.write(f"*Email:* {email}")
    st.write(f"*Phone:* {phone}")
    st.write(f"*Address:* {address}")
    st.write(f"*Education:* {education}")
    st.write(f"*Skills:* {', '.join(skills)}")
  
