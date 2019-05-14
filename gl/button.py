import pygame
from enum import Enum
from infrastructure.command import CommandType

class ButtonState(Enum):
    SELECTED = 1
    UNSELECTED = 2

class Button:
    def __init__(self, color, x, y, width, height, text='', command=0):
        self.color = color
        self.original_color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.state = ButtonState.UNSELECTED
        self.command = command
    
    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4, 0))
        
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 30, 1)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def hit(self, pos):
        if pos[0]  > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False

    def toggle_select(self):
        if self.state == ButtonState.UNSELECTED:
            self.state = ButtonState.SELECTED
            self.color = (int(self.color[0] * 0.8),int(self.color[1] * 0.8),int(self.color[2] * 0.8))

        else:
            self.state = ButtonState.UNSELECTED
            self.color = self.original_color

    def set_color(self, color):
        self.color = color
