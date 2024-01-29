import PySimpleGUI as sg

sg.theme('Light Green')

# 1- the layout
layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

# 2 - the window
window = sg.Window('Pattern 2', layout)

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Select the "output" text element and set the text to the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

# 4 - the close
window.close()
