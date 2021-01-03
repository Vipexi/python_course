#! /usr/bin/python3

if __name__ == "__main__":

    filename = "fibonacci_series_no_commas.txt"
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
            fibonacci_list=str(fibonacci_list)     
            fibonacci_list = fibonacci_list.replace("," , "")
        return(fibonacci_list)

    number = 0
    x = range(1, 101)
    for i in x:
        number += 1
        print("Series until",i, fibonacci_numbers(number))
        file_to_write.write(f"Series until {i} {fibonacci_numbers(number)}\n")