import tkinter as tk
from tkinter import ttk, messagebox
import csv, os
from datetime import date

FILE_NAME = "health_data.csv"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Date","Name","BMI","Water","Sleep","Exercise","Mood","Symptoms","HealthScore"])

# COLORS
BG = "#FFF9E6"
C1, C2, C3, C4 = "#4ECDC4", "#FFE66D", "#A8E6CF", "#FF8E9E"
BTN = "#6C5CE7"
BTN2 = "#00B894"

root = tk.Tk()
root.title("My Best Health App - Colourful + Diet Plan")
root.geometry("900x750")
root.config(bg=BG)

head = tk.Frame(root, bg="#FF6B6B", height=80)
head.pack(fill="x")
tk.Label(head, text="🌈 MY BEST HEALTH APP", font=("Segoe UI Black", 22), bg="#FF6B6B", fg="white").pack(pady=5)
tk.Label(head, text="BMI • Diet Plan • Daily Tracker • Improvement Tips", font=("Segoe UI", 11), bg="#FF6B6B", fg="white").pack()

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background=BG)
style.configure("TNotebook.Tab", font=("Segoe UI Bold", 11), padding=[18, 10])
style.map("TNotebook.Tab", background=[("selected", BTN)], foreground=[("selected", "white")])

nb = ttk.Notebook(root)
nb.pack(fill="both", expand=True, padx=15, pady=15)

p1 = tk.Frame(nb, bg=C1)
p2 = tk.Frame(nb, bg=C2)
p3 = tk.Frame(nb, bg=C3)
p4 = tk.Frame(nb, bg=C4)
nb.add(p1, text=" 👤 Profile ")
nb.add(p2, text=" 💧 Daily Log ")
nb.add(p3, text=" 🍎 Diet Plan ")
nb.add(p4, text=" 📊 Result & Tips ")

def white_card(parent):
    fr = tk.Frame(parent, bg="white", bd=0)
    fr.pack(fill="x", padx=20, pady=12, ipadx=10, ipady=10)
    return fr

# PAGE 1
c1 = white_card(p1)
tk.Label(c1, text="Enter Your Details", font=("Segoe UI Bold", 15), bg="white").pack(anchor="w", padx=10, pady=5)
name_e = tk.Entry(c1, font=("Segoe UI", 12)); age_e = tk.Entry(c1, font=("Segoe UI", 12))
h_e = tk.Entry(c1, font=("Segoe UI", 12)); w_e = tk.Entry(c1, font=("Segoe UI", 12))
for txt, ent in [("Name", name_e), ("Age", age_e), ("Height cm", h_e), ("Weight kg", w_e)]:
    r = tk.Frame(c1, bg="white"); r.pack(fill="x", padx=10, pady=4)
    tk.Label(r, text=txt+":", width=12, anchor="w", bg="white", font=("Segoe UI", 11, "bold")).pack(side="left")
    ent.pack(side="left", fill="x", expand=True, padx=10)

bmi_lbl = tk.Label(p1, text="BMI: --", font=("Segoe UI Black", 20), bg=C1); bmi_lbl.pack()
tip_lbl = tk.Label(p1, text="", font=("Segoe UI", 11), bg=C1, fg="#2D3436", wraplength=700, justify="left"); tip_lbl.pack(pady=5)

def calc_bmi():
    try:
        h = float(h_e.get())/100; w = float(w_e.get())
        bmi = w/(h*h)
        bmi_lbl.config(text=f"BMI: {bmi:.1f}")
        if bmi < 18.5:
            msg = "UNDERWEIGHT\nImprove: Need more protein & calories.\nEat: Ghee rice, eggs, milk, banana, peanut butter, nuts."
        elif bmi < 24.9:
            msg = "PERFECT FIT 😍\nImprove: Maintain same diet + exercise.\nEat: Balanced - 1 cup rice, dal, curd, veggies, fruits, 2L water."
        elif bmi < 29.9:
            msg = "OVERWEIGHT\nImprove: Reduce oil & rice, walk 45 min.\nEat: 2 chapati, salads, sprouts, green tea. Avoid biryani, sweets, cool drinks."
        else:
            msg = "OBESE - Need Attention\nImprove: Strict diet + daily walk + 3L water.\nEat: Only millets, oats, veggies, fruits. No fried, no sugar. Consult doctor."
        tip_lbl.config(text=msg)
        messagebox.showinfo("BMI Result", msg)
        return bmi
    except:
        messagebox.showerror("Error", "Enter Height & Weight correctly!"); return None

tk.Button(p1, text="✨ CALCULATE BMI", bg=BTN, fg="white", font=("Segoe UI Bold", 12), bd=0, padx=20, pady=8, command=calc_bmi).pack(pady=10)

# PAGE 2
c2 = white_card(p2)
tk.Label(c2, text="Daily Health Log", font=("Segoe UI Bold", 15), bg="white").pack(anchor="w", padx=10)
water_v = tk.DoubleVar(value=2.0); sleep_v = tk.DoubleVar(value=7.0); ex_v = tk.IntVar(value=30)
mood_v = tk.StringVar(value="Happy 😊")
for lbl, var, frm, to in [("Water (L)", water_v, 0, 5), ("Sleep (Hrs)", sleep_v, 0, 12), ("Exercise (Min)", ex_v, 0, 120)]:
    r = tk.Frame(c2, bg="white"); r.pack(fill="x", padx=10, pady=6)
    tk.Label(r, text=lbl, width=14, bg="white", font=("Segoe UI", 11, "bold")).pack(side="left")
    tk.Scale(r, variable=var, from_=frm, to=to, orient="horizontal", bg="white", troughcolor=C2, length=300, highlightthickness=0).pack(side="left")

r = tk.Frame(c2, bg="white"); r.pack(fill="x", padx=10, pady=6)
tk.Label(r, text="Mood", width=14, bg="white", font=("Segoe UI", 11, "bold")).pack(side="left")
ttk.Combobox(r, textvariable=mood_v, values=["Happy 😊","Energetic ⚡","Tired 😴","Stressed 😰","Sad 😔"], width=28).pack(side="left")

sym_vars = {}
c2b = white_card(p2)
tk.Label(c2b, text="Any Symptoms Today?", font=("Segoe UI Bold", 12), bg="white").pack(anchor="w", padx=10)
for s in ["Fever 🤒","Cold 🤧","Headache 🤕","Stomach Pain","Cough","Body Pain"]:
    v = tk.BooleanVar(); sym_vars[s]=v
    tk.Checkbutton(c2b, text=s, variable=v, bg="white", font=("Segoe UI", 10)).pack(anchor="w", padx=20)

# PAGE 3 DIET
c3 = white_card(p3)
tk.Label(c3, text="🍽️ Your Daily Diet Plan to Follow", font=("Segoe UI Bold", 14), bg="white", fg="#D63031").pack(anchor="w", padx=10)
diet_text = """
⏰ 7 AM: Warm water + 5 soaked almonds + Chia seeds

🥣 8:30 AM Breakfast: 2 Idli + Sambar OR Oats + Curd + Banana OR 2 Chapati + 2 Egg Whites

🍛 1:30 PM Lunch: 1 Cup Rice + Dal + Green Curry + Curd + Chicken/Fish (3x week)
       Avoid: Extra oil, pickle, fry

🍎 5 PM Snack: Roasted Chana / Sundal / Guava / Apple (NO biscuits/chips)

🌙 8 PM Dinner: 2 Chapati + Veg Curry + Salad OR Ragi Sangati + Sambar
       After 9:30 PM - No food

❌ AVOID: Cool drinks, Pizza, Burger, Maida, Sweets, Deep Fry
✅ MUST: 1 Fruit, 1 Bowl Curd, More Veggies, 3L Water

Tip: Walk 45 mins daily!
"""
tk.Label(c3, text=diet_text, font=("Segoe UI", 10), bg="white", justify="left", anchor="w").pack(padx=10, pady=5)

# PAGE 4 RESULT
c4 = white_card(p4)
tk.Label(c4, text="📊 Health Score & Improvement Tips", font=("Segoe UI Bold", 14), bg="white").pack(anchor="w", padx=10)
result_box = tk.Text(c4, height=18, font=("Segoe UI", 10), bg="#2D3436", fg="#00FFC6")
result_box.pack(fill="both", padx=10, pady=10)

def save_and_analyze():
    bmi = calc_bmi()
    if bmi is None: return
    score = 100; tips = []
    if water_v.get() < 2: score -= 15; tips.append("→ Low Water! Drink 3L daily (Removes tiredness)")
    if sleep_v.get() < 6: score -= 15; tips.append("→ Low Sleep! Sleep 7-8 hrs")
    if ex_v.get() < 20: score -= 20; tips.append("→ No Exercise! Walk 45 mins daily")
    if bmi >= 25: score -= 20; tips.append("→ High BMI! Reduce oil, rice, sweets")
    if bmi < 18.5: score -= 15; tips.append("→ Low Weight! Eat more protein (Milk, Eggs, Nuts)")
    sym_list = [k for k,v in sym_vars.items() if v.get()]
    if sym_list: score -= len(sym_list)*5
    status = "Excellent Health 🌟" if score>=80 else "Good, but need improvement 🙂" if score>=60 else "Need Attention ⚠️"
    final_msg = f"Date: {date.today()}\nName: {name_e.get()}\nBMI: {bmi:.1f}\nWater: {water_v.get()}L, Sleep: {sleep_v.get()}Hrs, Exercise: {ex_v.get()}Min\nMood: {mood_v.get()}\nSymptoms: {', '.join(sym_list) if sym_list else 'None'}\n\nHealth Score: {score}/100 - {status}\n\nIMPROVEMENT PLAN:\n" + "\n".join(tips) + "\n\nDIET TO FOLLOW:\n" + ("High Protein Diet" if bmi<18.5 else "Balanced Maintenance Diet" if bmi<25 else "Low Carb Fat Loss Diet")
    result_box.delete("1.0", tk.END); result_box.insert(tk.END, final_msg)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([date.today(), name_e.get(), f"{bmi:.1f}", water_v.get(), sleep_v.get(), ex_v.get(), mood_v.get(), ", ".join(sym_list), score])
    messagebox.showinfo("Saved!", f"Health Score: {score}/100\n{status}\n\nCheck Page 4 for full tips!")

tk.Button(p4, text="💾 SAVE & GET MY DIET + TIPS", bg=BTN2, fg="white", font=("Segoe UI Black", 13), bd=0, padx=30, pady=12, command=save_and_analyze).pack(pady=10)
tk.Label(root, text="Note: Wellness tracker only, not medical advice. Consult doctor if ill.", bg=BG, fg="gray", font=("Segoe UI", 8)).pack()
root.mainloop()