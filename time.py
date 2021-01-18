#! /usr/bin/python3

import time

start_time = time.time()
print(start_time)
for x in range(1000):
    for y in range(1000):
        xy = x+y
        print(xy, end=" ")
end_time = time.time()
print(end_time)
print(" ")
print(end_time - start_time)

for y in range(10):
    print(str(y) + " ", end="")
    time.sleep(1)

time_now = time.time()
print(time_now)
time.ctime(time_now)