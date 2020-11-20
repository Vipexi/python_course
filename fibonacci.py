#! /usr/bin/python3

"""def fibonacci_numbers():
    numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))
    fibonacci_list = [0,1]
    if numbers_in_series > 2:
        for i in range(2, numbers_in_series):
            nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2]
            fibonacci_list.append(nextnumber)
    print(fibonacci_list)
    

fibonacci_numbers()"""

"""def fibonacci_normal():
    numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))
    fibonacci_list = [0,1]
    if numbers_in_series > 2:
        for i in range(2, numbers_in_series):
            nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2]
            fibonacci_list.append(nextnumber)
        list_of_lists=[]
        sum1=sum(fibonacci_list)
        last_number=fibonacci_list[-1]
        list_of_lists.append(fibonacci_list)
        list_of_lists.append(sum1)
        list_of_lists.append(last_number)
    print(list_of_lists)
    
    

fibonacci_normal()"""

import statistics

def fibonacci_hard():
    numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))
    fibonacci_list = [0,1]
    if numbers_in_series > 2:
        for i in range(2, numbers_in_series):
            nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2]
            fibonacci_list.append(nextnumber)
        list_of_lists=[]
        sum1 = sum(fibonacci_list)
        last_number = fibonacci_list[-1]
        fibonacci_tuple = tuple(fibonacci_list)
        tuple_median = statistics.median(fibonacci_tuple)
        average_of_tuple = sum1 / len(fibonacci_tuple)
        list_of_lists.append(fibonacci_tuple)
        list_of_lists.append(sum1)
        list_of_lists.append(last_number)
        list_of_lists.append(tuple_median)
        list_of_lists.append("Milla Jovovich")
        list_of_lists.append(average_of_tuple)
    print(list_of_lists)
    
fibonacci_hard()
    

    


