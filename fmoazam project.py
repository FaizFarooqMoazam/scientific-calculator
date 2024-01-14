#Project purpose: to create a program which acts as a calculator which can solve a couple of types of questions.

import math

def _sine_function(angle_in_degrees): #Helper function used in sine rule function
    angle_in_radians = math.radians(angle_in_degrees) #Converts angle in degrees to radians
    sine_value = math.sin(angle_in_radians)
    return sine_value

def sine_function():
    angle_in_degrees = float(input("What is your angle? : "))
    return _sine_function(angle_in_degrees)

def cosine_function():
    angle_in_degrees = float(input("What is your angle? : "))
    angle_in_radians = math.radians(angle_in_degrees) #Converts angle in degrees to radians
    cosine_value = math.cos(angle_in_radians)
    return cosine_value

def factorial_function(x):
    fact_final = 1
    for i in range ( 1 , x + 1):
        fact_final = fact_final * i
    return fact_final

def sum_of_arithmetic_series():
    n = float(input('How many terms would you like to determine the sum of? --> '))
    a = float(input('What is the first term in the arithmetic series? --> '))
    d = float(input('What is the common difference of your arithmetic series? --> '))
    sum_arithmetic = n/2*(2*a+(n-1)*d)
    return sum_arithmetic

def sum_of_geometric_series():
    n = float(input('How many terms would you like to determine the sum of? --> '))
    a = float(input('What is the first term in the geomtric series? --> '))
    r = float(input('What is the common ratio of your geometric series? --> '))
    sum_geometric = a*((1-r**n)/(1-r))
    return sum_geometric

def is_prime(x):
    factor_count = 0
    prime = False
    for i in range (1 , x + 1):
        if x % i == 0:
            factor_count = factor_count + 1
    print("Number of factors = " + str(factor_count))
    if factor_count == 2:
        prime = True
    return prime

def _is_prime(x):    # Helper function for prime_numbers_between. Doesn't actually show you if a specific number is prime, but carries 
    factor_count = 0 #                                                                            out the same function and is used in
    prime = False    #                                                                            prime_numbers_between.
    for i in range (1 , x + 1):
        if x % i == 0:
            factor_count = factor_count + 1
    if factor_count == 2:
        prime = True
    return prime

def prime_numbers_between(): # This is inclusive of integer_1 & integer_2
    integer_1 = input("Your first number: ")
    integer_2 = input("Your last number: ")
    primeList = []
    for i in range ( integer_1 , integer_2 + 1 ):
        if _is_prime(i):
            primeList.append(i)
    return primeList


def tangent_function():
    angle_in_degrees = float(input("What is your angle? : "))
    angle_in_radians = math.radians(angle_in_degrees) #Converts angle in degrees to radians
    tangent_value = math.tan(angle_in_radians)
    return tangent_value


def sine_rule_function (): #Finds the length of an unknown side based on a side and 2 angles. 
    side_length_1 = (input('Enter the length of the side known: '))
    angle_1 = (input('Enter the corresponding angle: '))
    angle_2 = (input('Enter the angle corrseponding to the unknown side: '))
    side_length_1 = float(side_length_1)
    angle_1 = float(angle_1)
    angle_2 = float(angle_2)
    side_length_2 = (side_length_1/_sine_function(angle_1))*_sine_function(angle_2)
    return side_length_2


if __name__ == "__main__":
    print("Welcome to the Math Function Calculator!")
    print("Please select an option:")
    print("1. Sine Function")
    print("2. Cosine Function")
    print("3. Tangent Function")
    print("4. Factorial Function")
    print("5. Sum of Arithmetic Series")
    print("6. Sum of Geometric Series")
    print("7. Check if a Number is Prime")
    print("8. Prime Numbers Between Two Integers")
    print("9. Sine Rule Function")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        result = sine_function()
        print("Sine value:", result)
    elif choice == 2:
        result = cosine_function()
        print("Cosine value:", result)
    elif choice == 3:
        result = tangent_function()
        print("Tangent value:", result)
    elif choice == 4:
        x = int(input("Enter a number: "))
        result = factorial_function(x)
        print("Factorial:", result)
    elif choice == 5:
        result = sum_of_arithmetic_series()
        print("Sum of arithmetic series:", result)
    elif choice == 6:
        result = sum_of_geometric_series()
        print("Sum of geometric series:", result)
    elif choice == 7:
        x = int(input("Enter a number: "))
        result = is_prime(x)
        print("Is prime:", result)
    elif choice == 8:
        prime_list = prime_numbers_between()
        print("Prime numbers:", prime_list)
    elif choice == 9:
        result = sine_rule_function()
        print("Result of Sine Rule Function:", result)
    else:
        print("Invalid choice. Please select a valid option.")