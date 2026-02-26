import random

#add validate function for guess to replace first few if statements

def prompt_for_guess():
    target = random.randrange(1, 101)
    while True:
        user_input = input('Guess the number between 1 and 100: ')
        try:
            guess = int(user_input)
        except:
            print('Please guess an integer')
            continue

        if guess < 1:
            print('Integer must be 1 or higher')
        elif guess > 100:
            print('Integer must be 100 or lower')
        elif guess > target:
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

