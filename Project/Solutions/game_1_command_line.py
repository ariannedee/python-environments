import click

from word_game.game import WordGame


@click.command()
@click.argument('num', default=6)
@click.option('--hard', is_flag=True)
def game(num, hard):
    WordGame(num_wrong_guesses=num, hard_word=hard).play_game()


if __name__ == '__main__':
    game()
