#fileNotFound
# with open("file.txt", "r") as file:
#     file.read()

# KeyError
# a_dictionary= {"key": "value"}
# value = a_dictionary("non_existent_key")

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("a_text.txt", "r")
except:
    file = open("a_text.txt", "w")