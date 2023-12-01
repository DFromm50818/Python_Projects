print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input('You came to a crossroad. You feel the beautiful Treasure is near. Which direction you want to go. "left" or "right?" ')
direction_lower = direction.lower()

if direction_lower == "left":
  action = input('You see a large river. There is a ferryman on the other side of the river, his Boat drives really slow and you mention. Perhaps i am faster when i swim. Do you want to "swim" or "wait"? ')
  action_lower = action.lower()
  
  if action_lower == "wait":
    door = input('You came to a house with three doors and a floor that leads futher into the house. The doors are "Red", "Blue" and "Yellow" or you go thorugth the "Floor"? ')
    door_lower = door.lower()

    if door_lower == "red":
      print("You came into the room and the door closed after you. You can't open the door and starved to death. Game Over!")
    elif door_lower == "blue":
      print("You opened the door and a monster kills you instantly. Game Over!")
    elif door_lower == "floor":
      print("You goes along the way and you can't await to find the treasure. After a long walk you mentioned that you were here before. You try to go back, but you can't... Game over!")
    else:
      print("You opened the yellow door and found the treasure. You win!")
    
  else:
    print("You were drowned by attacking trouts. Game Over!")
    
else:
  print("You go along the way und fall into a traphole. Game Over!")