#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
first_index = int(position[0]) -1
second_index = int(position[1]) -1
if first_index <= 3 and second_index <= 3: 
    #print(f"first_index: {first_index}, second_index: {second_index}")
    map[first_index][second_index] = "X"
else:
    print("index out of range")




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

