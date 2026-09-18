import gradio as gr
import csv
import os
from datetime import date

FILE_NAME = "health_data.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Date","Name","BMI","Water","Sleep","Exercise","Mood","Symptoms","HealthScore"])

def save_data(name, bmi, water, sleep, exercise, mood, symptoms, health_score):
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([str(date.today()), name, bmi, water, sleep, exercise, mood, symptoms, health_score])
    
    # Show saved data
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = f.read()
    
    return f"✅ Saved Pavani! {name} data saved on {date.today()}\n\n{data}"

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue"), title="My Health App") as app:
    gr.Markdown("# ❤️ My Health Tracker - Pavani's App")
    gr.Markdown("Daily health details enter chey!")
    
    with gr.Row():
        name = gr.Textbox(label="Name", value="Pavani")
        bmi = gr.Number(label="BMI", value=22.5)
    
    with gr.Row():
        water = gr.Number(label="Water (Liters)", value=2.0)
        sleep = gr.Number(label="Sleep (Hours)", value=7.0)
    
    with gr.Row():
        exercise = gr.Number(label="Exercise (Mins)", value=30)
        health_score = gr.Slider(1, 10, value=7, label="Health Score")
    
    mood = gr.Dropdown(["Happy", "Tired", "Stressed", "Energetic", "Normal"], label="Mood", value="Happy")
    symptoms = gr.Textbox(label="Symptoms (if any)", placeholder="Any symptoms?")
    
    btn = gr.Button("Save Data", variant="primary")
    output = gr.Textbox(label="Saved Data", lines=15)
    
    btn.click(fn=save_data, inputs=[name, bmi, water, sleep, exercise, mood, symptoms, health_score], outputs=output)

app.launch()
