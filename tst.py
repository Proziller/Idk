import tkinter as tk

root = tk.Tk()
class q ():
    def __init__(self):
        self.button = tk.Button(root, text="Original Text")
        self.button.pack()

    def change_button_text(self):
        self.button.config(text="New Text")

    def play(self):
        self.button.config(command=self.change_button_text)
        root.mainloop()

q.play(self)