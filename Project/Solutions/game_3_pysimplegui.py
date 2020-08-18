import PySimpleGUI as sg

from word_game.game import WordGame

game = WordGame()

# Set theme
sg.theme('Material2')

# Set layout
buttons_row_1 = []
buttons_row_2 = []
for char in "abcdefghijklmnopqrstuvwxyz".upper():
    if char < 'N':
        buttons_row_1.append(sg.Button(char))
    else:
        buttons_row_2.append(sg.Button(char))

layout = [[sg.Text('Guess the word'), sg.Text(size=(24, 1))],
          [sg.Text(''), sg.Text(size=(24, 1), key='-DISPLAY-')],
          [sg.Text(''), sg.Text(size=(16, 1), key='-STATE-')],
          buttons_row_1,
          buttons_row_2]

# Create window
window = sg.Window('Guessing game', layout)
window.finalize()

# Set initial state
window['-DISPLAY-'].update(game.display_word)
window['-STATE-'].update(f'{game.wrong_guesses_left} wrong guesses left')

# Event loop (wait for event and react)
while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
    game.guess_letter(event)
    window['-DISPLAY-'].update(game.display_word)
    new_status = ''
    window[event].Update(disabled=True)
    if game.game_won():
        new_status = 'You won!'
    elif game.game_lost():
        new_status = 'You lost'
    else:
        new_status = f'{game.wrong_guesses_left} wrong guesses left'

    window['-STATE-'].update(new_status)

# Close window
window.close()
