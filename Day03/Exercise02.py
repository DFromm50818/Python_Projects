# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height**2)
int_bmi = int(bmi)

if bmi < 18.5:
    print(f"Your BMI is {int_bmi}, you are underweight.")

elif bmi < 25:
    print(f"Your BMI is {int_bmi}, you have a normal weight.")

elif bmi < 30:
    print(f"Your BMI is {int_bmi}, you are slightly overweight.")

elif bmi < 35:
    print(f"Your BMI is {int_bmi}, you are obese.")

elif bmi > 35:
    print(f"Your BMI is {int_bmi}, you are clinically obese.")
else:
    print("")