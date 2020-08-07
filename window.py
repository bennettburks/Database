from tkinter import *
from os import path
import json

class Window():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.window = Tk()

    def window(self):
        return self.window

    def initialize(self):
        self.window.title("Database")
        self.window.geometry("800x800")

    def create(self):
        left_window_init(self.window)
        right_window_init(self.window)
        self.window.mainloop()

    

#shows all of JSON file
#TODO: reorganize file
def left_window_init(window):
    left_window = LabelFrame(window, text="File Contents")
    left_window.pack(fill="both", expand="yes", padx=10, pady=10, side=LEFT)

    json_text = Text(left_window)
    json_text.insert(INSERT, check_file())
    json_text.pack()

#shows JSON tags
#TODO: reorganize file
def right_window_init(window):
    right_window = LabelFrame(window, text="Database Tags")
    right_window.pack(fill="both", expand="yes", padx=10, pady=10, side=RIGHT)

    json_tags = Text(right_window)
    for itm in get_tags():
        json_tags.insert(INSERT, (itm + "\n"))

    json_tags.pack()


def check_file():
    if not path.exists("data.json"):
        json_file = open("data.json", "x")
        json_file.close()
    with open("data.json", "r") as json_file:
        json_text = json.loads(json_file.read())
        return str(json_text)

def get_tags():
    with open("data.json", "r") as json_file:
        json_text = json.loads(json_file.read())
        return json_text.keys()