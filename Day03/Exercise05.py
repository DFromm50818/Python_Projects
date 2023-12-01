# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_lower1 = name1.lower()
name_lower2 = name2.lower()

T = (name_lower1.count("t")) + (name_lower2.count("t"))
R = (name_lower1.count("r")) + (name_lower2.count("r"))
U = (name_lower1.count("u")) + (name_lower2.count("u"))
E = (name_lower1.count("e")) + (name_lower2.count("e"))

result_true = T + R + U + E

L = (name_lower1.count("l")) + (name_lower2.count("l"))
O = (name_lower1.count("o")) + (name_lower2.count("o"))
V = (name_lower1.count("v")) + (name_lower2.count("v"))
E = (name_lower1.count("e")) + (name_lower2.count("e"))

result_love = L + O + V + E

result = str(result_true) + str(result_love)
result_int = int(result)

if(result_int < 10) or (result_int > 90):
    print(f"Your score is {result_int}, you go together like coke and mentos.")

elif(result_int > 40) and (result_int < 50):
    print(f"Your score is {result_int}, you are alright together.")

else:
    print(f"Your score is {result_int}.")


