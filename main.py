# import the pygame module, so you can use it
import pygame
import gl.window as glw
from infrastructure.command import CommandType

window_width = 800
window_height = 600

button_width = (window_height - 100) /8
button_height = button_width
button_color_light = (195, 195, 195)
button_color_dark = (100, 100, 100)
button_start_x = window_width/2 - 4*button_width
button_start_y = window_height/2 - 4*button_height

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
            window.add_button(colors[j], x, y, button_width, button_height, '', CommandType.MOVE)
            x += button_width
        
        y += button_height
                



def main():
    window = glw.Window(window_width, window_height, (255, 255, 255))
    add_buttons(window)
    window.on_execute()


if __name__=="__main__":
    main()