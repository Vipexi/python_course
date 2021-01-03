#! /usr/bin/python3

import statistics

if __name__ == "__main__":

    filename = "fibonacci.csv"
    try:
        file_to_write = open(filename,"a")

    except:
        print("cannot open file")
    
    file_to_write.write("Fibonacci series from 1 to 100:\n")


    def fibonacci_numbers(numbers_in_series):
        fibonacci_list = [1]
        if numbers_in_series >= 1:
            for i in range(1,numbers_in_series): 
                nextnumber = fibonacci_list [i-1] + fibonacci_list[i-2] 
                fibonacci_list.append(nextnumber)
            sum_of_all = sum(fibonacci_list)
            median_of_fibonacci = statistics.median(fibonacci_list)
            average_of_fibonacci = sum_of_all / len(fibonacci_list)
            fibonacci_list.append(sum_of_all)
            fibonacci_list.append(median_of_fibonacci)
            fibonacci_list.append(average_of_fibonacci)
            fibonacci_list = str(fibonacci_list)     
            fibonacci_list = fibonacci_list.replace("," , "")
            
        return(fibonacci_list)
        

    
    number = 0
    x = range(1, 101)
    for i in x:
        number += 1
        print("Series until",i, fibonacci_numbers(number))
        file_to_write.write(f"Series until {i} {fibonacci_numbers(number)}")