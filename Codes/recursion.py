'''
In Recursion, a function calls itself repeatedly.
Each recursive call works on a smaller or simpler subproblem,
 and the process continues until it reaches a base case,
 which stops the recursion


Recursive Case

The part of the function where it calls itself on a smaller/simpler input.

Base Case

A condition that stops the recursion to prevent infinite loops.
'''

#factorial using recursion


def factorial(n):
    #Base Case

    if n==0:
        return 1

    #Recursive case

    else:
        return  n * factorial(n-1)


print(factorial(10))