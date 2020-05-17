from tkinter import Tk, Button

from ViewModule.ViewDesign import ViewDesign


class View:
    root: Tk

    def __init__(self):
        self.root = ViewDesign().root
        button: Button = self.root.children.get("my_button")
        a = button.config()
        print()

    # todo: add all handler

    def start(self):
        self.root.mainloop()
