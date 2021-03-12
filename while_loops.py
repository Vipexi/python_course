#! /usr/bin/python3

answer_from_user = " "
while True:
    print("outer while")
    while answer_from_user != "end":
        answer_from_user = input("if you want to end type: end")
        if answer_from_user != "end":
            print("so you want to keep going!")

while True:
    answer_from_user = input("if you want to end type: end")
    if answer_from_user == "end":
        break
    else:
        print("so you want to keep going!")