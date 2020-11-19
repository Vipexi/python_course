#! /usr/bin/python3

while True:
    try:
        number = int(input("give a number:"))
        break
    except:
        print("give a number in digits, like a 2")
print(number)