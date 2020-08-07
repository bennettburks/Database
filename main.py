#main file with intialization 
from tkinter import *
from os import path
import json

def main():
    window = Tk()
    window.title("Database")
    window.geometry("800x600")

    left_window = LabelFrame(window, text="File Contents")
    left_window.pack(fill="both", expand="yes", padx=10, pady=10)

    json_text = Text(left_window)
    json_text.insert(INSERT, check_file())
    json_text.pack()

    window.mainloop()


def check_file():
    if not path.exists("data.json"):
        json_file = open("data.json", "x")
        json_file.close()
    with open("data.json", "r") as json_file:
        json_text = json.loads(json_file.read())
        return str(json_text)


if __name__ == "__main__":
    main()


