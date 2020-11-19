#! /usr/bin/python3

dice_d6 = []
for i in range(1,7):
    dice_d6.append(i)

print(dice_d6)
dice_d6.pop()
print(dice_d6)

"""long_list = [i for i in range(100,201)]
short_list = [i for i in range(10)]
print(long_list)
print(short_list)
index = 5
short_list[index] = long_list[index*9]
print(short_list)"""