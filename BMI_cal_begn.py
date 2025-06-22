#BMI CALCULATOR FOR BEGINNERS

#step1: add a user input.
weight = float(input("Enter the weight in kilograms(kg):"))
height = float(input("Enter the height in meters(m):"))

#step2: calculate bmi
bmi = weight / (height**2)
print(f"Your bmi is: {bmi:.2f}")

#step3: classified the category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif 25<= bmi < 30:
    category = "Overweight"
else: 
    category = "Obese"

print("You are calssified as:", category)       
