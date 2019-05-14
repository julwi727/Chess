# import the pygame module, so you can use it
import pygame
import gl.window as glw
from infrastructure.command import CommandType
import gui_id as gui

window_width = 1440
window_height = 900

button_width = int((window_height - 100) /8)
button_height = button_width
button_color_light = (195, 195, 195)
button_color_dark = (100, 100, 100)
button_start_x = int(window_width/2 - 4*button_width)
button_start_y = int(window_height/2 - 4*button_height)

print("Button width: " + str(button_width))
print("Button height: " + str(button_height))
print("Button start x: " + str(button_start_x))
print("Button start y: " + str(button_start_y))

def add_buttons(window):
    y = button_start_y

    for i in range(8):
        light_first = i%2 == 0
        x = button_start_x

        colors = [
            button_color_dark,
            button_color_light,
            button_color_dark,
            button_color_light,
            button_color_dark,
            button_color_light,
            button_color_dark,
            button_color_light
        ]

        if light_first:
            colors = [
                button_color_light,
                button_color_dark,
                button_color_light,
                button_color_dark,
                button_color_light,
                button_color_dark,
                button_color_light,
                button_color_dark
            ]

        for j in range(8):
            window.add_button(colors[j], x, y, button_width, button_height, -1, '', CommandType.SELECT_PIECE)
            x += button_width
        y += button_height

def main():
    window = glw.Window(window_width, window_height, (255, 255, 255))
    add_buttons(window)
    window.add_text_box((255, 255, 255), 10, button_start_y, button_start_x - 20, 700, gui.LEFT_TEXT_BOX)
    window.add_button((100, 100, 100), button_start_x/2 - 100 - 5   , button_start_y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Clear text', CommandType.CLEAR_TEXT)
    window.add_button((100, 100, 100), button_start_x/2 + 5         , button_start_y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Add row', CommandType.ADD_ROW)
    window.on_execute()


if __name__=="__main__":
    main()