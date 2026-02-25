import random

#add validate function for guess to replace first few if statements

while True:
    target = 50 # make random
    input = input('Guess the number between 1 and 100: ')
    guess = int(input)

    if type(guess) != 'int':
        print('Please guess an integer')
        # return to input
    elif guess < 1:
        print('Integer must be 1 or higher')
        # return to input
    elif guess > 100:
        print('Integer must be 100 or lower')
        # return to input
    elif guess > target:
        print('Lower!')
        # return to input
    elif guess < target:
        print('Higher!')
        # return to input
    elif guess == target:
        print(f'Congratulations, the correct answer was {guess}')
        break

