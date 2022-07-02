import math
import random
import os
import path

path_to_here = os.path.dirname(os.path.realpath(__file__))
path_test = "C:/Users/benca/PycharmProjects/AsciiArt/Help_Menu"


def help_output():
    f = open(path_test, "r")
    print(f.read())


class Manager:
    def __init__(self):
        self.is_running = True
        self.is_printing = False
        self.h = 5
        self.w = 10
        self.bg = "."

    def user_command(self, fetched_command):
        if fetched_command == "quit":
            self.is_running = False
        elif fetched_command == "help":
            help_output()
        elif fetched_command == "toggle print":
            self.is_printing = not self.is_printing
        elif fetched_command == "set size":
            self.change_size()
        elif fetched_command == "background":
            self.bg = input("new background: ")
        else:
            pass

    def change_size(self):
        height = input("height: ")
        if height.isnumeric():
            self.h = int(height)
        else:
            print("value can only be integer")

        width = input("width: ")
        if width.isnumeric():
            self.w = int(width)
        else:
            print("value can only be integer")
