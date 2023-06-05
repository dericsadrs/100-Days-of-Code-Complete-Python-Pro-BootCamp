# from turtle import Turtle, Screen

# #object
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

#new object
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle","Charmander"])
table.add_column("Type",["Electric", "Water","Fire"])

table.align = "l"

print(table)