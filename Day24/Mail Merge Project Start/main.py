#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# My solution:

list_names = []
with open("./Input/Names/invited_names.txt", "r") as file:
    names_raw = file.readlines()

for name in names_raw:
    name_pur = name.strip("\n")
    list_names.append(name_pur)

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

for name in list_names:
    with open(f"./Output/ReadyToSend/invitation_letter_{name}.txt", "w") as file:
        invitation = letter.replace("[name]", name)
        file.write(invitation)


# Angelas Solution:

# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
