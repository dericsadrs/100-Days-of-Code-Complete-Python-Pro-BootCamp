#
# Created on Sun Jun 04 2023
# Created by Software Engineer Deric San Andres
#

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")