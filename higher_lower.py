import random

def prompt_for_guess():
    target = random.randrange(1, 101)
    number_of_guesses = 0
    def validate_integer_in_range(user_input_string):
        try:
            user_integer = int(user_input_string)
        except:
            return False

        if user_integer < 1 or user_integer > 100:
            return False

        return True

    while True:
        user_input = input('Guess the number from 1 to 100: ')
        if validate_integer_in_range(user_input) == False:
            print('Please guess an integer from 1 to 100')
        else:
            guess = int(user_input)
            if guess > target:
                number_of_guesses += 1
                print('Lower!')
            elif guess < target:
                number_of_guesses += 1
                print('Higher!')
            elif guess == target:
                number_of_guesses += 1
                print(f'Congratulations, the correct answer was {guess}! It took you {number_of_guesses} guesses.')

                def play_again_prompt():
                    return input('Play again? Y/N: ')
                play_again_response = play_again_prompt().lower()

                if play_again_response == 'y':
                    prompt_for_guess()
                elif play_again_response == 'n':
                    break
                else:
                    print('Please answer Y or N')
                    play_again_prompt()
                break

if __name__ == '__main__':
    prompt_for_guess()

