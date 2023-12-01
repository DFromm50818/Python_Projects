# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

student_average = 0
person_heights = int(n + 1)

for heights in student_heights:
    student_average += heights

print(round(student_average / person_heights))