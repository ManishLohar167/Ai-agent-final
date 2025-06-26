import streamlit as st
import requests

st.set_page_config(page_title="Appointment Booking AI", layout="centered")
st.title("🤖 Appointment Booking AI Agent")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
date = st.date_input("Appointment Date")
time = st.time_input("Preferred Time")

if st.button("Book Appointment"):
    data = {
        "name": name,
        "email": email,
        "date": str(date),
        "time": str(time)
    }
    with st.spinner("Booking your appointment..."):
        response = requests.post("http://localhost:8000/book", json=data)
        if response.status_code == 200:
            st.success("✅ Appointment booked successfully!")
        else:
            st.error("❌ Failed to book appointment.")
