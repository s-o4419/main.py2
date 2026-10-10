
from tkinter import Tk
from gui import RobotGUI


def main():
    window = Tk()
    app = RobotGUI(window)
    window.mainloop()


    if _name_ == "_main_":
        main()
        