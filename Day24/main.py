# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

with open("my_file.txt", mode="a") as file:
    file.write("\nHach da is a ya.")

with open("C:/Users/Daniel Fromm/Desktop/new_file.txt", mode="w") as file:
    file.write("New Text here.")