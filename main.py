# import the pygame module, so you can use it
import pygame
import gl.window as glw
from infrastructure.command import CommandType
import gui_id as gui
import properties

def add_buttons(window):
    y = properties.BOARD_BUTTON_START_Y


    for i in range(8):
        light_first = i%2 == 0
        x = properties.BOARD_BUTTON_START_X

        colors = [
            properties.BUTTON_COLOR_DARK,
            properties.BUTTON_COLOR_LIGHT,
            properties.BUTTON_COLOR_DARK,
            properties.BUTTON_COLOR_LIGHT,
            properties.BUTTON_COLOR_DARK,
            properties.BUTTON_COLOR_LIGHT,
            properties.BUTTON_COLOR_DARK,
            properties.BUTTON_COLOR_LIGHT
        ]

        if light_first:
            colors = [
                properties.BUTTON_COLOR_LIGHT,
                properties.BUTTON_COLOR_DARK,
                properties.BUTTON_COLOR_LIGHT,
                properties.BUTTON_COLOR_DARK,
                properties.BUTTON_COLOR_LIGHT,
                properties.BUTTON_COLOR_DARK,
                properties.BUTTON_COLOR_LIGHT,
                properties.BUTTON_COLOR_DARK
            ]

        for j in range(8):
            window.add_button(colors[j], x, y, properties.BOARD_BUTTON_WIDTH, properties.BOARD_BUTTON_WIDTH, -1, '', CommandType.SELECT_PIECE)
            x += properties.BOARD_BUTTON_WIDTH
        y += properties.BOARD_BUTTON_HEIGHT

def init_gui(window):
    add_buttons(window)
    window.add_text_box((255, 255, 255), 10, properties.BOARD_BUTTON_START_Y, properties.BOARD_BUTTON_START_X - 20, 700, gui.LEFT_TEXT_BOX)
    window.add_button(properties.BUTTON_COLOR_LIGHT, properties.BOARD_BUTTON_START_X/2 - 100 - 5   , properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Clear text', CommandType.CLEAR_TEXT)
    window.add_button(properties.BUTTON_COLOR_LIGHT, properties.BOARD_BUTTON_START_X/2 + 5         , properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Add row', CommandType.ADD_ROW)
    

def main():
    window = glw.Window(properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT, (255, 255, 255))
    init_gui(window)
    window.on_execute()


if __name__=="__main__":
    main()