
# Function to calculate a factorial from the number provided then return that answer 
def factorial(number):
    solution = 1
    while number > 1: 
        solution = solution * number 
        number = number - 1

    print(solution)
    return solution # returns the solution to be used else where

def recursion_factorial(n):
    if n == 1:
        return 1
    else:
        return n*recursion_factorial(n-1)
    
n = int(input("What number do you want a factorial of? "))

def sum_of_numbers_to_n(n):
    if n == 1:
        return 1
    else:
        return n+sum_of_numbers_to_n(n-1)
    
def harmonic_calculator(n):
    if n == 1:
        return 1
    else:
        return 1/n +harmonic_calculator(n-1)
    
def fibonacci_calc(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else: 
        return fibonacci_calc(num-1) + fibonacci_calc(num-2)
    
def sum_n_in_list(list):
    length = len(list)-1
    if length == 0:
        return list[0]
    else:
        return list.pop(length) + sum_n_in_list(list)

        

list = [4,7,8,23,14,87,45,76,12,23,5,7,9,1,2,7,34]

print(sum_n_in_list(list))
#print(fibonacci_calc(number))
