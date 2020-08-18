"""
A word guessing game
Run from the command line
Accepts an optional "num" argument for the number of wrong guesses allowed (default is 6)
Accepts an optional "--hard" flag to play with a hard word
"""
import click

from word_game.game import WordGame


@click.command()
@click.argument('num', default=6)
@click.option('--hard', is_flag=True)
def game(num, hard):
    WordGame(num_wrong_guesses=num, hard_word=hard).play_game()


if __name__ == '__main__':
    game()
