print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))

    if age < 12:
        print("Please pay $5.")
    elif age > 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
       bill+=3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")