#file that initializes GUI

from tkinter import *
from os import path
import json

window = Tk()
window.title("Database")
window.geometry("800x800")

def window_start():
    window_init()    #initializes all visual data in database
    window.mainloop()

#shows all of JSON file
#TODO: reorganize file
def window_init():
    #left window init
    left_window = LabelFrame(window, text="File Contents")
    left_window.pack(fill="both", expand="yes", padx=10, pady=10, side=LEFT)

    json_text = Text(left_window)
    json_text.insert(INSERT, check_file())
    json_text.pack()

    #right window init
    right_window = LabelFrame(window, text="Database Tags")
    right_window.pack(fill="both", expand="yes", padx=10, pady=10, side=RIGHT)

    json_tags = Listbox(right_window)
    for itm in get_tags():
        json_tags.insert(END, itm)
    json_tags.pack()
    #lambda allows called function to have parameters
    json_button = Button(right_window, text="Update Database", command=lambda: update_json_text(json_text))
    json_button.pack()

def update_json_text(json_text):
    json_text.delete("1.0", END)
    json_text.insert(END, "test input")

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