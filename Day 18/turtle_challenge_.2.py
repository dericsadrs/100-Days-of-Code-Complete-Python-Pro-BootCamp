#
# Created on Wed Jun 07 2023
# Created by Software Engineer Deric San Andres
#

import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()