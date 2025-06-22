import tkinter as tk
from tkinter import messagebox


bmi_history = [] 


def calculate_bmi():
    global bmi_history

    try:
        # Input weight and height
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate input
        if weight <= 0 or height <= 0:
            raise ValueError

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI result
        bmi_result_label.config(text=f"Your BMI: {bmi:.2f}")

        # Categorize the result
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        category_label.config(text=f"Category: {category}")

        # Store result in history
        bmi_history.append((weight, height, round(bmi, 2), category))

        # Update history display
        update_history()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers greater than 0.")

def update_history():
    global bmi_history
    history_text.delete('1.0', tk.END)
    for entry in bmi_history:
        history_text.insert(
            tk.END,
            f"Weight: {entry[0]} kg, Height: {entry[1]} m, BMI: {entry[2]}, Category: {entry[3]}\n"
        )


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Input Section
tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Button to Calculate
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result Display
bmi_result_label = tk.Label(root, text="Your BMI:", font=('Arial', 12))
bmi_result_label.pack(pady=5)

category_label = tk.Label(root, text="Category:", font=('Arial', 12))
category_label.pack(pady=5)

# History Display
tk.Label(root, text="BMI History", font=('Arial', 12, 'bold')).pack(pady=10)
history_text = tk.Text(root, height=10, width=45)
history_text.pack(pady=5)

# Start the GUI
root.mainloop()
