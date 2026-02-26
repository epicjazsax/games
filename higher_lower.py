import random

def prompt_for_guess():
    target = random.randrange(1, 101)
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
                print('Lower!')
            elif guess < target:
                print('Higher!')
            elif guess == target:
                print(f'Congratulations! The correct answer was {guess}.')

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

