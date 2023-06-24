#
# Created on Sat Jun 24 2023
# Created by Software Engineer Deric San Andres
#

from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = miles + 1.689
    kilometer_result_label.config(text= f"[km]")
    
    
window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry(width = 7)
miles_input.grid(column = 1, row = 0)

miles_label = label(text= "Miles")
miles_label.grid(column = 2, row = 8)

is_equal_label = label(text ="is equal to")
miles_label.grid(column = 8, row = 1)


kilometer_result_label =  Label(text = "0")
kilometer_result_label.grid(column = 1, row = 1)

kilometer_label = Label(text = "Km")

calculate_button = Button(text = "Calculate")