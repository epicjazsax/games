from random import randint
from pretty_list import pretty_list as pretty


def get_selection(prompt, options):
    """loop asking for input until user response is within given options"""
    while True:
        response = input(f'{prompt} [{pretty(options, True)}]: ')
        if response in options:
            return response
        else:
            print('not a valid response')


def resolve(player_guess, computer_guess):
    """resolve winner of rock, paper, scissors battle"""
    play_options = ['rock', 'paper', 'scissors']
    message = ['you win!', 'computer wins :(', 'tie. no one wins']
    if player_guess and computer_guess in play_options:
        result = ((play_options.index(player_guess) - play_options.index(computer_guess)) + 2) % 3
        return message[result]


def rock_paper_scissors():
    """play rock, paper, scissors on repeat until user doesn't want to continue"""
    while True:
        play_options = ['rock', 'paper', 'scissors']
        computer_guess = play_options[randint(0, 2)]
        player_guess = get_selection('make your selection!', play_options)
        print(f'computer chose {computer_guess}')
        resolution = resolve(player_guess, computer_guess)
        print(resolution)
        play_again = get_selection('do you want to continue?', ['yes', 'no'])
        if play_again == 'no':
            print('have a nice day <3')
            break


if __name__ == '__main__':
    rock_paper_scissors()
    