import pygame
import gl.button as glb
import gl.text_box as gltb
import infrastructure.command as cmd
import gui_id as gui
import game.board
import properties
from pygame.locals import *
 
class Window:
    def __init__(self, width, height, fill_color):
        self._running = True
        self.fill_color = fill_color
        self._display_surf = None
        self.size = self.width, self.height = width, height
        self.buttons = []
        self.text_boxes = []
        self.selected_button = None
        self.message_queue = cmd.command_queue
        self.board = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._display_surf.fill(self.fill_color)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.check_clicks(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            self.deselect_last()
            self.check_command(pygame.mouse.get_pos())

    def on_loop(self):
        if self.message_queue.has_message():
            command = self.message_queue.get_message()
            
            if command[0] == cmd.CommandType.MOVE:
                print("Move")

            if command[0] == cmd.CommandType.SELECT_PIECE:
                print("Select")

            if command[0] == cmd.CommandType.CLEAR_TEXT:
                self.clear_text(command[1])

            if command[0] == cmd.CommandType.ADD_ROW:
                self.add_row(command[1], command[2])

            if command[0] == cmd.CommandType.MAKE_MOVE:
                self.board.make_move()

            if command[0] == cmd.CommandType.RESET_BOARD:
                self.board.reset()

        
    def on_render(self):
        self._display_surf.fill(self.fill_color)
        for button in self.buttons:
            button.draw(self._display_surf)
        
        for text_box in self.text_boxes:
            text_box.draw(self._display_surf)

        if self.board:
            self.board.draw(self._display_surf)

        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    #====GUI methods====
    def add_board(self, board):
        self.board = board

    def add_button(self, color, x, y, width, height, component_id, text='', command=''):
        self.buttons.append(glb.Button(color, x, y, width, height, component_id, text, command))
    
    def add_text_box(self, color, x, y, width, height, component_id):
        self.text_boxes.append(gltb.TextBox(color, x, y, width, height, component_id))

    def check_clicks(self, pos):
        for button in self.buttons:
            if button.hit(pos):
                button.toggle_select()
                self.selected_button = button

    def check_command(self, pos):
        for button in self.buttons:
            if button.hit(pos):
                self.message_queue.add_message(button.command, button.component_id)

        self.board.check_command(pos)

    def deselect_last(self):
        if self.selected_button != None:
            self.selected_button.toggle_select()
            self.selected_button = None

    def clear_text(self, component_id):
        print("Clear text_box with id: " + str(component_id))
        for text_box in self.text_boxes:
            if text_box.component_id == component_id:
                text_box.clear()

    def add_row(self, component_id, text):
        print("Add row to text_box with id: " + str(component_id))
        for text_box in self.text_boxes:
            if text_box.component_id == component_id:
                text_box.add_row(text)
