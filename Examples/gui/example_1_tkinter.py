import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.text = 'Hello'
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, {'text': 'This is a heading'}, font=("Helvetica", 24))
        self.label.pack(pady=20, padx=30)

        self.string_variable = tk.StringVar()
        self.string_variable.set(self.text)
        self.word_state = tk.Label(self, textvariable=self.string_variable)
        self.word_state.pack()

        self.input = tk.Entry(self)
        self.input.pack(side=tk.LEFT, padx=20, pady=20)

        self.button = tk.Button(self)
        self.button["text"] = 'Save'
        self.button["command"] = self.save_btn
        self.button.pack(side=tk.LEFT, padx=20, pady=20)

    def save_btn(self):
        self.text = self.input.get()
        self.string_variable.set(self.text)
        self.input.delete(0, len(self.text))


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
