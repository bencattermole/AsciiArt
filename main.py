import os
import random
import math
import Input_Manager as Im

app_mngr = Im.Manager()


def main():

    while app_mngr.is_running:

        if app_mngr.is_printing:
            box_print(app_mngr.h, app_mngr.w, app_mngr.bg)
        user_says = input("command: ")

        app_mngr.user_command(user_says)


def box_print(height, width, background):
    bar = "|"
    line = "-"
    corner = "+"
    empty = background

    print(f"{corner}{line * width}{corner}")

    for row in range(height):
        print(f"{bar}{empty * width}{bar}")

    print(f"{corner}{line * width}{corner}")


def read_from_pickle(path):
    pass


if __name__ == '__main__':
    main()