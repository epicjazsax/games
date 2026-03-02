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
    play_options = ['rock', 'paper', 'scissors']
    message = ['you win!', 'computer wins :(', 'tie. no one wins']
    if player_guess and computer_guess in play_options:
        result = ((play_options.index(player_guess) - play_options.index(computer_guess)) + 2) % 3
        return message[result]


def rock_paper_scissors():
    while True:
        computer_guess = PLAY_OPTIONS[randint(0, 2)]
        player_guess = get_selection()
        print(f'computer chose {computer_guess}')
        resolution = resolve(player_guess, computer_guess)
        print(resolution)
        play_again = input('do you want to continue? yes or no: ')
        if play_again == 'no':
            print('have a nice day <3')
            break


if __name__ == '__main__':
    rock_paper_scissors()
    
