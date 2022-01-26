"""
Word guessing game. When player guesses 6 wrong letters, they lose.
"""
from .data import get_random_word

print("hello")

class WordGame(object):
    def __init__(self, hard_word=False, num_wrong_guesses=6):
        self.word = get_random_word().lower().strip()
        self.guessed_letters = []
        self.wrong_guesses_left = num_wrong_guesses
        print(f'New game created{": hard mode" if hard_word else ""}')

    @property
    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_'
                         for letter in self.word])

    def guess_is_correct(self, guess):
        return guess in self.word

    def game_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def game_lost(self):
        return self.wrong_guesses_left == 0

    def game_over(self):
        return self.game_lost() or self.game_won()

    def play_game(self):
        while True:
            # Display current state of the game
            print(self.display_word)
            print(f'Guessed letters: {" ".join(self.guessed_letters) if len(self.guessed_letters) else "None"}')
            print(f'Guesses left: {self.wrong_guesses_left}\n')

            # Get a guess from the user
            guess = input('Guess a letter: ')
            print()

            correct = self.guess_letter(guess)
            if correct:
                print('Correct!')
            else:
                print('Nope!')

            # Check to see if they won or lost
            if self.game_won():
                print(f'You won :) The word was "{self.word}"')
                return
            elif self.game_lost():
                print(f'You lost :( The word was "{self.word}"')
                return

    def guess_letter(self, guess):
        guess = guess.lower()
        self.guessed_letters.append(guess)
        if self.guess_is_correct(guess):
            correct = True
        else:
            self.wrong_guesses_left -= 1
            correct = False
        return correct


if __name__ == '__main__':
    game = WordGame()
    game.play_game()
