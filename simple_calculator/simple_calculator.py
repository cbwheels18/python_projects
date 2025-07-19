def add(first, second):
    sum = (float(first) + float(second))
    return sum

def subtract(first, second):
    difference = (float(first) - float(second))
    return difference

def divide(first, second):
    quotient = (float(first) / float(second))
    return quotient

def multiply(first, second):
    product = (float(first) * float(second))
    return product

def equation(calculation):
    part1, part2, part3 = calculation.split(' ')
    if part1 == '(':
        part1 = '*'
        combined = part1 * part2
    else:
        part1 = part1
    if part2 == '+':
        combined = part1 + part3
    total = combined

    return total

user_input = ''
first_input = ''
second_input = ''

while user_input != 'exit':
    user_input = input('Welcome to the calculator, add. subtract, multiply, or divide? ')
    if user_input == 'add':
        first_input = input('Please enter the first number to add: ')
        second_input = input('Please enter the second number to add: ')
        sum = add(first_input, second_input)
        print(sum)
    elif user_input == 'subtract':
        first_input = input('Please enter the first number to subtract: ')
        second_input = input('Please enter the second number to subtract: ')
        difference = subtract(first_input, second_input)
        print(difference)
    elif user_input == 'multiply':
        first_input = input('Please enter the first number to multiply: ')
        second_input = input('Please enter the second number to multiply: ')
        product = multiply(first_input, second_input)
        print(product)
    elif user_input == 'divide':
        first_input = input('Please enter the first number to divide: ')
        second_input = input('Please enter the second number to divide: ')
        quotient = divide(first_input, second_input)
        print(quotient)
    elif user_input == 'equation':
        user_input = input('Please type out the equation: ')
        total = equation(user_input)
        print(total)
    elif user_input == 'exit':
        print('Thanks for using the calculator!')
    else:
        print('Incorrect input, try again!')