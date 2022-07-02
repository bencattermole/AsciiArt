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

    seed = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"

    coord_dict = get_coords(seed, app_mngr.w, app_mngr.h)
    print(coord_dict)

    print(f"{corner}{line * width}{corner}")

    for row in range(height):
        row_string = f"{bar}"
        for column in range(width):
            # print(f"this is row: {row}")
            # print(f"this is column: {column}")
            if (column, row) in coord_dict:
                row_string = row_string + str(coord_dict[(column, row)])
            else:
                row_string = row_string + empty

        print(row_string + f"{bar}")

    print(f"{corner}{line * width}{corner}")


def get_coords(seed, center_x, center_y):
    coord_list = [(int(center_x/2), int(center_y/2))]
    coord_dict = {}
    step_in_hex = generate_steps(seed)

    step_logic = {
        "00": [-1, 1],
        "01": [1, 1],
        "10": [-1, -1],
        "11": [1, -1]
    }

    binary_step = []

    for hex_step in step_in_hex:
        b = bin(hex_step)[2:]
        if not len(b) % 2:
            binary_step.append(b)
        else:
            select = str(random.randint(0, 1))
            binary_step.append((b + select))

    for c_l in binary_step:
        n = 2
        test = [c_l[i:i + n] for i in range(0, len(c_l), n)]
        for pair in test:
            start_c = coord_list[-1]
            move_like = step_logic[pair]

            if 0 > start_c[0]+move_like[0] or start_c[0]+move_like[0] >= app_mngr.w:
                x_comp = start_c[0]
            else:
                x_comp = start_c[0]+move_like[0]

            if 0 > start_c[1]+move_like[1] or start_c[1]+move_like[1] >= app_mngr.h:
                y_comp = start_c[1]
            else:
                y_comp = start_c[1]+move_like[1]

            end_c = (x_comp, y_comp)
            coord_list.append(end_c)

    for coord in coord_list:

        if coord in coord_dict:
            pass
        else:
            weight = coord_list.count(coord)
            coord_dict.update({coord: weight})

    return coord_dict


def generate_steps(seed):
    array_of_chars = list(seed)
    array_of_values = []

    for char in array_of_chars:
        array_of_values.append(ord(char))

    return array_of_values


if __name__ == '__main__':
    main()
