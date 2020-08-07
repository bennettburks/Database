#main file with intialization 
from window import Window


def main():
    window = Window("Database", "800x800")
    window.initialize()
    window.create()

if __name__ == "__main__":
    main()


