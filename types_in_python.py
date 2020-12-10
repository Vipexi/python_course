#! /usr/bin/python3

import numpy as np
import random
import math

x = np.array([1,], dtype=np.uint8)

#print(x)

x[0] = 14

#print(type(x[0]))

x[0] = 400

#print(x)

x[0] = -4

#print(x)

#print(bin(x[0]))

#print(bin(-4))

y = np.array([1,], dtype=np.uint8)

y[0] = -252

#print(bin(y[0]))

# 0000 0000 = integrer 1000 0011

first_dict = {"name":"Johan","age":24,"is alive": True}

#print(first_dict["name"])
first_dict["height"]= 175

#print(first_dict)

first_dict.update({"name":"Saana"})

#print(first_dict)

car_dict = {"Model":"family-vehicle","engine size":"150Horsepower","weight":"1000kg","top speed":"200km/h"}
bike_dict = {"Model":"Bomber","engine size":"1000kwh","weight":"120kg","top speed":"200km/h"}
jet_dict = {"Model": "Jumbo","engine size":"Jumbo","weight": "10000kg","top speed":"10000km/h"}

vehicle_dict = { 
    "car1":car_dict,
    "bike1":bike_dict,
    "jet1":jet_dict
}
#print(vehicle_dict)

#print(vehicle_dict)

"""mathematical_constants = {
    "pi":"3.14159 26535",
    "e":"2.71828 18284",
    "sqrt2":"1.41421",
    "sqrt3":"1.73205 08075",
    "sqrt5":"2.360679774",
    "gamma": "0.57721 56649",
    "varphi":"1.61803 39887"
    }

def math_randomizer(answer):
    random_int = random.randint(0,200)
    divider = random.choice(list(mathematical_constants.values()))
    answer= random_int / divider
    return answer

print(math_randomizer())"""

    
    

#print(mathematical_constants)

