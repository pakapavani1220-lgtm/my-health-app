import streamlit as st
import csv
import os
from datetime import date

FILE_NAME = "health_data.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Date","Name","BMI","Water","Sleep","Exercise","Mood","Symptoms","HealthScore"])

st.set_page_config(page_title="My Health App", page_icon="❤️")
st.title("❤️ My Health Tracker")
st.write("Daily health details enter chey Pavani!")

with st.form("health_form"):
    name = st.text_input("Name", value="Pavani")
    bmi = st.number_input("BMI", min_value=10.0, max_value=40.0, value=22.5)
    water = st.number_input("Water (Liters)", min_value=0.0, value=2.0)
    sleep = st.number_input("Sleep (Hours)", min_value=0.0, value=7.0)
    exercise = st.number_input("Exercise (Mins)", min_value=0, value=30)
    mood = st.selectbox("Mood", ["Happy", "Tired", "Stressed", "Energetic", "Normal"])
    symptoms = st.text_input("Symptoms (if any)")
    health_score = st.slider("Health Score", 1, 10, 7)
    
    submitted = st.form_submit_button("Save Data")
    
    if submitted:
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([str(date.today()), name, bmi, water, sleep, exercise, mood, symptoms, health_score])
        st.success(f"Saved! {name} health data saved on {date.today()}")

st.divider()
st.subheader("📊 Saved Data")
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = list(csv.reader(f))
        if len(data) > 1:
            st.table(data)
        else:
            st.info("Inka data ledu. Form fill chesi Save chey.")
