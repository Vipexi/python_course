#! /usr/bin/python3


import random
"""class Rand_string:
    def rand_num(self):
        x = 10
        num = random.randrange(0,x)
        string = str(num)
        return string
test = Rand_string()
test.x = 5
d = test.rand_num()
print(d)"""

class Car:
    def __init__(self,weight,doors,manufacturer,model):
        self.weight = weight
        self.doors = doors
        self.manufacturer = manufacturer
        self.model = model
    def my_car(self):
        print("Manufacturer: "+ str (self.manufacturer))
        print("Model: "+ str (self.model))
        print("Weight: "+ str (self.weight))
        print("Foors: "+ str (self.doors))

mondeo = Car(1450,4,"ford","mondeo")
mondeo.my_car()
    
        

    