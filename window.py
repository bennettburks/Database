#file that initializes GUI

from tkinter import *
from os import path
import json

window = Tk()
window.title("Database")
window.geometry("800x800")

#global so other functions can access easily
left_window = LabelFrame(window, text="File Contents")
right_window = LabelFrame(window, text="Database Tags")
bottomright_window = LabelFrame(window, text="JSON Info")

def window_start():
    window_init()    #initializes all visual data in database
    window.mainloop()

#shows all of JSON file
#TODO: reorganize file
def window_init():
    #left window init
    left_window.pack(fill="both", expand="yes", padx=10, pady=10, side=LEFT)

    text = Text(left_window)
    text.insert(INSERT, str(file_contents()))
    text.pack()

    #right window init
    right_window.pack(fill="both", expand="yes", padx=10, pady=10, side=RIGHT)

    tags = Listbox(right_window)
    for itm in get_tags():
        tags.insert(END, itm)
    tags.pack()
    #lambda allows called function to have parameters
    json_button = Button(right_window, text="Update Database", command=lambda: update_text(text, tags))
    json_button.pack()

    #json window init
    bottomright_window.pack(fill="both", expand="yes", padx=10, pady=10, side=BOTTOM)

#updates left text box
def update_text(text, tags):
    data = file_contents()
    data = data[tags.get(ACTIVE)]
    text.delete("1.0", END)
    text.insert(END, data)
    window_data(text, data)

def window_data(text, data):
    for itm in bottomright_window.winfo_children():
            itm.destroy()
    if data_is_collection(data) is True:
        print(data.keys())
        for itm in data.keys():
            print(f"{itm} - {data[itm]}")
            text = Label(bottomright_window, text=f"{itm}:")
            text.pack()
            itm = Entry(bottomright_window)
            itm.pack()
        print(bottomright_window.winfo_children())
        update = Button(bottomright_window, text="Update Collection")
        update.pack()


#checks if data type has multiple objects
def data_is_collection(data):
    if type(data) is dict or type(data) is list or type(data) is tuple or type(data) is set:
        return True
    else:
        return False

#creates data file if it doesn't exist
def check_file():
    if not path.exists("data.json"):
        json_file = open("data.json", "x")
        json_file.close()

#returns data file contents (dictionary)
def file_contents():
    check_file()
    with open("data.json", "r") as json_file:
        text = json.loads(json_file.read())
        return text

#returns tags of dictionary from data file
def get_tags():
    with open("data.json", "r") as json_file:
        text = json.loads(json_file.read())
        return text.keys()