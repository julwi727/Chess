import pygame
from enum import Enum

class Row:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def clear(self):
        self.text = ""

class TextBox:
    def __init__(self, color, x, y, width, height, component_id):
        self.component_id = component_id
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = []
        self.text_size = 10
        self.current_row = 0

        row_y = self.y

        for i in range(int(self.height/self.text_size)):
            self.rows.append(Row(self.x, row_y, self.width, self.text_size, "Row " + str(i)))
            row_y += self.text_size
            self.current_row = i

    def clear(self):
        for row in self.rows:
            row.clear()
            self.current_row = 0

    def add_row(self, text):
        self.rows[self.current_row].text = text
        self.current_row += 1
        if self.current_row == len(self.rows) - 1:
            self.current_row -= 1
    
    def draw(self, window):
        #Outline
        #pygame.draw.rect(window, (0,0,0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4, 0))
        
        #Background rect
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        #Each row
        for row in self.rows:
            font = pygame.font.SysFont('arial', self.text_size, 1)
            text = font.render(row.text, 1, (0, 0, 0))
            window.blit(text, (row.x + (self.width/2 - text.get_width()/2), row.y + (row.height/2 - text.get_height()/2)))


