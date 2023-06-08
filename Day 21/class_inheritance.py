#
# Created on Wed Jun 07 2023
# Created by Software Engineer Deric San Andres
#
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
    def play_dead(self):
        print("I'm dead don't eat me")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        super().play_dead()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()