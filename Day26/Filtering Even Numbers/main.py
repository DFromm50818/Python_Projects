list_of_strings = input().split(",")

list_of_integers = [int(number) for number in list_of_strings]
result = [even_number for even_number in list_of_integers if (even_number % 2) == 0]

print(result)