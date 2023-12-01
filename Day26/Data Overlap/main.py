with open("file1.txt", "r") as file:
    raw_list_1 = file.readlines()
with open("file2.txt", "r") as file:
    raw_list_2 =  file.readlines()

result = [int(num) for num in raw_list_1 if num in raw_list_2]
print(result)