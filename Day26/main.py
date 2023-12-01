# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)


## Python List Comprehension

# numbers = [1, 2, 3]
# new_list =[n + 1 for n in numbers] # [new_item for item in list]
# print(new_list)
#
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
#
# num_list = [number * 2 for number in range(1,5)]
# print(num_list)


## Conditional List Comprehension

# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)


## Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

## Conditional Dictionary Comprehension

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student:random.randint(1,100) for student in names}
# passed_students = {student: value for (student, value) in students_score.items() if value > 60}
# print(passed_students)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
## Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

## Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(key)

## Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student =="Angela":
        print(row.score)