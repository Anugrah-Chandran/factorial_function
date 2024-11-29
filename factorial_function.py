'''Author: Anugrah Chandran
Date : 29-11-24
Description : Program to find the factorial of a number using Recursion.'''
def factorial(num):
    if num == 0:
        return 1
    else:
        return(num*factorial(num-1))

num = int(input("Enter a number: "))
factorial(num)
print("The factorial of the number is",factorial(num))
