from random import randint

PLAY_OPTIONS = ['rock', 'paper', 'scissors']

def get_selection():
    while True:
        response = input('Choose rock, paper, or scissors: ')
        if response in PLAY_OPTIONS:
            return response
        else:
            print('not a valid response')


def resolve(player_guess, computer_guess):
    message = ['you win!', 'computer wins :(', 'tie. no one wins']
    if player_guess and computer_guess in PLAY_OPTIONS:
        result = ((PLAY_OPTIONS.index(player_guess) - PLAY_OPTIONS.index(computer_guess)) + 2) % 3
        return message[result]

def play_again_prompt():
    while True:
        def prompt_user():
            return input('Play again? Y/N: ')
        user_response = prompt_user().lower()

        if user_response == 'y':
            return True
        elif user_response == 'n':
            return False
        else:
            print('Invalid answer')
            continue

def rock_paper_scissors():
    while True:
        computer_guess = PLAY_OPTIONS[randint(0, 2)]
        player_guess = get_selection()

        resolution = resolve(player_guess, computer_guess)
        print(f'computer chose {computer_guess}')
        print(resolution)

        play_again_response = play_again_prompt()

        if play_again_response == True:
            rock_paper_scissors()
        break

if __name__ == '__main__':
    rock_paper_scissors()
    
