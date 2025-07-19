import random

def computer_guess():
    print('Think of a number between 1 and 100...')
    print('I am going to guess what number you have, each time I guess tell me if it is higher or lower...')
    print('Once I guess it right you can type correct')
    low = 1
    high = 100
    rand_number = 0
    hl_input = ''

    while hl_input != 'correct':
        rand_number = random.randint(low, high)
        print(f'My guess is {rand_number}')
        hl_input = input('higher, lower, or correct? ')
        if hl_input == 'higher':
            low = rand_number
        elif hl_input == 'lower':
            high = rand_number
        elif hl_input == 'correct':
            print('I told you I was going to guess your number...')
        else:
            print('incorrect value')

computer_guess()