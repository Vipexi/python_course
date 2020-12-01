#! /usr/bin/python3

import os

filename = "test_file3.txt"

try:
    open(filename ,"w").write("example file with some text")

except:
    print("file saving failed")

open(filename,"w").write("write more text to file\n")

open(filename,"a").write("second line to file\n")

content_of_the_file = open(filename,"r").read()

print(content_of_the_file)

with open(filename) as file:
    content_of_the_file2 = file.read()

print(content_of_the_file2)

print(file.closed)

file2 = open(filename,"r")

content_of_the_file3 = file2.read()

print(content_of_the_file3)

print(file2.closed)

file2.close()

print(file2.closed)

open(filename,"a").write("second line to file\n")

open(filename,"a").write("second line to file\n")

open(filename,"a").write("3. line to file\n")

file2 = open(filename,"r")

line_from_file = file2.readline()

print(line_from_file)

for line in file2:
    print(line)

file2.close()

file2 = open(filename,"r")

for line in file2:
    print(line)

file2=open(filename,"a")

file2.write("another thing to the file")

file2.close()

file2 = open(filename,"a+")

line_from_file = file2.readline()

print(line_from_file)

file2.read()

file2.write("just some text")

line_from_file = file2.readline()

print(line_from_file)

file2.read()

number = 5

file2.write(str(number))

file2.write(f"something {number}")

file2.close()

file2 = open(filename,"r")

file2.read()




