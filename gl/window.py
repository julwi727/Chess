import pygame
import gl.button as glb
import infrastructure.command as cmd
from pygame.locals import *
 
class Window:
    def __init__(self, width, height, fill_color):
        self._running = True
        self.fill_color = fill_color
        self._display_surf = None
        self.size = self.width, self.height = width, height
        self.buttons = []
        self.selected_button = None
        self.message_queue = cmd.Command()
 
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
            
            if command == cmd.CommandType.MOVE:
                print("Move")
            if command == cmd.CommandType.SELECT_PIECE:
                print("Select")
        
    def on_render(self):
        self._display_surf.fill(self.fill_color)
        for button in self.buttons:
            button.draw(self._display_surf)
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

    def add_button(self, color, x, y, width, height, text='', command=''):
        self.buttons.append(glb.Button(color, x, y, width, height, text, command))
    
    def check_clicks(self, pos):
        for button in self.buttons:
            if button.hit(pos):
                button.toggle_select()
                self.selected_button = button

    def check_command(self, pos):
        for button in self.buttons:
            if button.hit(pos):
                self.message_queue.add_message(button.command)

    def deselect_last(self):
        if self.selected_button != None:
            self.selected_button.toggle_select()
            self.selected_button = None