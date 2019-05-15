# import the pygame module, so you can use it
import pygame
import gl.window as glw
from infrastructure.command import CommandType
import gui_id as gui
import properties
import game.board


def init_gui(window):
    window.add_text_box(properties.TEXT_BOX_BG_COLOR,   properties.GLOBAL_MARGIN,                       properties.BOARD_BUTTON_START_Y, properties.BOARD_BUTTON_START_X - 20, 700, gui.LEFT_TEXT_BOX)
    window.add_button(properties.BUTTON_COLOR_LIGHT,    properties.BOARD_BUTTON_START_X/2 - 100 - 5   , properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Clear text', CommandType.CLEAR_TEXT)
    window.add_button(properties.BUTTON_COLOR_LIGHT,    properties.BOARD_BUTTON_START_X/2 + 5         , properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Add row', CommandType.ADD_ROW)
    window.add_button(properties.BUTTON_COLOR_LIGHT,    properties.BOARD_END_X , properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Make move', CommandType.MAKE_MOVE)
    window.add_button(properties.BUTTON_COLOR_LIGHT,    properties.WINDOW_WIDTH - properties.ACTION_BUTTON_WIDTH*2 + properties.GLOBAL_MARGIN/2, properties.BOARD_BUTTON_START_Y + 700 + 10, 100, 20, gui.LEFT_TEXT_BOX, 'Reset board', CommandType.RESET_BOARD)
    

def main():
    window = glw.Window(properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT, (255, 255, 255))
    init_gui(window)
    window.add_board(game.board.Board())
    window.on_execute()


if __name__=="__main__":
    main()