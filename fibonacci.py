#! /usr/bin/python3

fibonacci_200 = fibonacci(200)
print(fibonacci_200)
fibonacci_70= fibonacci(70)
print(fibonacci_70)

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(9))
 