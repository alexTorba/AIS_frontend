from tkinter import *


class ViewDesign:
    root: Tk

    def __init__(self):
        self.root = Tk()
        Button(self.root, name="my_button", text="Hello")
        Button(self.root, text="Hello2")
        # create all design
