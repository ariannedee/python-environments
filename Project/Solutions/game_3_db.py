import tkinter as tk
from functools import partial

from word_game import game


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.game = game.WordGame(with_db=True, hard_word=True)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, {'text': 'Guess the word'}, font=("Helvetica", 24))
        self.title.pack(pady=20)

        self.display_word = tk.StringVar()
        self.display_word.set(self.game.display_word)
        self.word_state = tk.Label(self, textvariable=self.display_word, font=("Helvetica", 24))
        self.word_state.pack()

        self.game_state = tk.StringVar()
        self.game_state.set(f'{self.game.wrong_guesses_left} wrong guesses left')
        self.wrong_guesses = tk.Label(self, textvariable=self.game_state)
        self.wrong_guesses.pack(pady=10)

        self.buttons = []
        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.frame1.pack(padx=40)
        self.frame2.pack(padx=40, pady=30)
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if letter <= 'N':
                frame = self.frame1
            else:
                frame = self.frame2
            button = tk.Button(frame)
            button["text"] = letter
            button["command"] = partial(self.guess_letter(button))
            button.pack(side=tk.LEFT)
            self.buttons.append(button)

    def update_state(self):
        if self.game.game_over():
            self.display_word.set(self.game.word.upper())
            for button in self.buttons:
                button['state'] = 'disabled'
        else:
            self.display_word.set(self.game.display_word.upper())
            self.game_state.set(f'{self.game.wrong_guesses_left} wrong guesses left')

        if self.game.game_lost():
            self.game_state.set('You lost')
        elif self.game.game_won():
            self.game_state.set(f'You won!')
        self.update_idletasks()

    def guess_letter(self, button):
        letter = button['text']

        def inner():
            self.game.guess_letter(letter)
            self.update_state()
            button["state"] = "disabled"

        return inner


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
