#! /usr/bin/python3

# First I made an input to ask the user how many numbers of the fibonacci the user wants to know.
# Until I asked others how they had done it. 
# But the code worked also with asking a answer input for how many numbers the user wanted to know.
# Wasn't sure if the task was to use input or change the code for every single time when we run the code.
"""numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))"""

# So I made a function with a list, that discludes number 0,1 because it is something that doesn't need counting
# and you wouldn't want to know 0 or 1 fibonacci numbers to begin with?
if __name__ == "__main__":

    filename = "fibonacci_series_no_commas.txt"
    try:
        file_to_write = open(filename,"a")

    except:
        print("cannot open file")
    
    file_to_write.write("Fibonacci series from 1 to 100:\n")

    def fibonacci_numbers(numbers_in_series):
        fibonacci_list = [1]
        if numbers_in_series >= 1: #The if-statement excludes number 0,1
            for i in range(1,numbers_in_series): #The for loop goes through the list in range of 2 to the number with the function was called
                nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2] #This variable sums the two previous numbers together,
                fibonacci_list.append(nextnumber) # i stands for the order of the number in the list given by The user.
            """fibonacci_list=str(fibonacci_list)     
            fibonacci_list = fibonacci_list.replace("," , "") # This appends the variable into the list I made previously."""
        return(fibonacci_list)

    number = 0
    x = range(1, 101)
    for i in x:
        number += 1
        print("Series until",i, fibonacci_numbers(number))
        file_to_write.write(f"Series until {i} {fibonacci_numbers(number)}\n")
    


# In the normal task I used the same format as easy until I made a new a list

"""numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))

def fibonacci_normal(numbers_in_series):
    fibonacci_list = [0,1]
    if numbers_in_series >= 2:
        for i in range(2,numbers_in_series):
            nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2]
            fibonacci_list.append(nextnumber)
        list_of_lists=[] # This list is where everything is gathered
        sum1=sum(fibonacci_list) # Made a variable that includes the sum of all the numbers in the list
        last_number=fibonacci_list[-1] # Made a variable that has the last number of the list
        list_of_lists.append(fibonacci_list) # Append the fibonaccilist in to the list of lists
        list_of_lists.append(sum1) # Append the sum to the list of lists
        list_of_lists.append(last_number) # And lastly the last number in the list
    return(list_of_lists)
    
    

normal=fibonacci_normal(30)
normal2=fibonacci_numbers(200)
print(normal)
print(normal2)

# This hard task is nearly the same as the two other ones. I imported statistics to get the median-function and get the median from the list.

 

# numbers_in_series=int(input("How many fibonacci numbers do you want to know?"))

import statistics

def fibonacci_hard(numbers_in_series):
    fibonacci_list = [0,1]
    if numbers_in_series >= 2:
        for i in range(2,numbers_in_series):
            nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2]
            fibonacci_list.append(nextnumber)
        list_of_lists=[]
        sum1 = sum(fibonacci_list)
        last_number = fibonacci_list[-1]
        fibonacci_tuple = tuple(fibonacci_list) # I made a variable and changed the list in to a tuple. Then stored the tuple inside the variable
        tuple_median = statistics.median(fibonacci_tuple) # This variable has the median of the tuple inside it.
        average_of_tuple = sum1 / len(fibonacci_tuple) # Here I count the average of the tuple. By dividing the sum with amount of elements in the tuple.
        list_of_lists.append(fibonacci_tuple) # Then I started appending all these variables in to the list of lists
        list_of_lists.append(sum1)
        list_of_lists.append(last_number)
        list_of_lists.append(tuple_median)
        list_of_lists.append("Milla Jovovich") # There's always a way to include Resident Evil in a Fibonacci series. :D
        list_of_lists.append(average_of_tuple)
    return(list_of_lists)
    
hard=fibonacci_hard(30)
print(hard)
hard2=fibonacci_hard(200)

print(hard2)"""



    


