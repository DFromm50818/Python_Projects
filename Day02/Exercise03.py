# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

rest = 90 - age_as_int
day = rest * 365
week = rest * 52
month = rest * 12

print (f"You have {day} days, {week} weeks, and {month} months left.") 