#! /usr/bin/python3

"""def function_with_return(input_to_function1, input_to_function2):
    variable_that_we_return_from_function = input_to_function1 + input_to_function2
    return variable_that_we_return_from_function


# call to function

answer_to_print1 = function_with_return(1,4)
print(answer_to_print1)"""

#easy1: modify function so that it takes 3 inputs instead of 2
#modify also function call, to call function with numbers 1,4,5

#easy2: make another function call with numbers 1,2,3
#and save that to variable answer_to_print2 and print that also

def function_with_return(input_to_function1, input_to_function2, input_to_function3 ):
    variable_that_we_return_from_function = input_to_function1 + input_to_function2 + input_to_function3
    return variable_that_we_return_from_function

def numbers(number_input1, number_input2, number_input3 ):
    returning_function = number_input1 + number_input2 + number_input3
    return returning_function

answer_to_print1 = function_with_return(1,4,5)
answer_to_print2 = numbers(1,2,3) 
print(answer_to_print1)
print(answer_to_print2)

