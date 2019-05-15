import game.pieces as pieces
import pygame
import properties
import gl.button
import infrastructure.log as log

class Square:
    def __init__(self, coordinates, x, y, color, width, height):
        self.coordinates = coordinates
        self.x = x
        self.y = y
        self.piece = None
        self.color = color
        self.width = width
        self.height = height
        self.original_color = color
        self.state = gl.button.ButtonState.UNSELECTED
    
    def add_piece(self, piece):
        self.piece = piece

    def clear_piece(self):
        self.piece = None

    def get_piece(self):
        return self.piece

    def get_icon(self):
        if self.piece:
            return self.piece.image_source

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.piece:
            x = self.x + self.width/4
            y = self.y + self.height/4
            rect = self.piece.get_image().get_rect()
            rect.center = (x, y)
            window.blit(self.piece.image, rect.center)

    def hit(self, pos):
        if pos[0]  > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False

    def toggle_select(self):
        if self.state == gl.button.ButtonState.UNSELECTED:
            self.state = gl.button.ButtonState.SELECTED
            self.color = (int(self.color[0] * 0.8),int(self.color[1] * 0.8),int(self.color[2] * 0.8))

        else:
            self.state = gl.button.ButtonState.UNSELECTED
            self.color = self.original_color


    def __str__(self):
        return str(self.piece) + " at " + str(self.coordinates)
        

class Board:
    def __init__(self):
        self.tiles = []
        self.selected_tiles = [None, None]

        y = properties.BOARD_BUTTON_START_Y
        for i in range(8):
            self.tiles.append([])
            x = properties.BOARD_BUTTON_START_X

            for j in range(8):
                color = properties.BUTTON_COLOR_DARK
                if i%2 == 0 and j%2 == 0:
                    color = properties.BUTTON_COLOR_LIGHT
                elif i%2 != 0 and j%2 != 0:
                    color = properties.BUTTON_COLOR_LIGHT
                
                self.tiles[i].append(Square((i, j), x, y, color, properties.BOARD_BUTTON_WIDTH, properties.BOARD_BUTTON_HEIGHT))
                x += properties.BOARD_BUTTON_WIDTH
            y += properties.BOARD_BUTTON_HEIGHT
        
        self.add_pieces()

    def make_move(self):
        if self.selected_tiles[0] != None and self.selected_tiles[1] != None:
            log.log("Moving " + str(self.selected_tiles[0]) + " to " + str(self.selected_tiles[1]))
            self.selected_tiles[0].toggle_select()
            self.selected_tiles[1].toggle_select()
            self.selected_tiles = [None, None]
        else:
            log.log("You need to select two tiles to make a move!")

    def reset(self):
        #reset the board to the original layout
        for row in self.tiles:
            for tile in row:
                tile.state = gl.button.ButtonState.SELECTED
                tile.toggle_select()
                tile.clear_piece()
                self.selected_tiles = [None, None]
        
        log.log("Resetting board")

        self.add_pieces()

    def add_pieces(self):
        #row 1(2) and row 6(7) shall have only pawns
        for tile in self.tiles[1]:
            tile.add_piece(pieces.Pawn_Black())
        
        for tile in self.tiles[6]:
            tile.add_piece(pieces.Pawn_White())

        #Add rooks
        self.tiles[0][0].add_piece(pieces.Rook_Black())
        self.tiles[7][0].add_piece(pieces.Rook_White())
        self.tiles[0][7].add_piece(pieces.Rook_Black())
        self.tiles[7][7].add_piece(pieces.Rook_White())

        #Add knights
        self.tiles[0][1].add_piece(pieces.Knight_Black())
        self.tiles[7][1].add_piece(pieces.Knight_White())
        self.tiles[0][6].add_piece(pieces.Knight_Black())
        self.tiles[7][6].add_piece(pieces.Knight_White())

        #Add bishops
        self.tiles[0][2].add_piece(pieces.Bishop_Black())
        self.tiles[7][2].add_piece(pieces.Bishop_White())
        self.tiles[0][5].add_piece(pieces.Bishop_Black())
        self.tiles[7][5].add_piece(pieces.Bishop_White())

        #Add queens
        self.tiles[0][3].add_piece(pieces.Queen_Black())
        self.tiles[7][4].add_piece(pieces.Queen_White())

        #Add kings
        self.tiles[0][4].add_piece(pieces.King_Black())
        self.tiles[7][3].add_piece(pieces.King_White())

    def draw(self, window):
        for row in self.tiles:
            for tile in row:
                tile.draw(window)

    def check_command(self, pos):
        for row in self.tiles:
            for tile in row:
                if tile.hit(pos):
                    print(str(tile) + " pressed!")
                    if self.selected_tiles[0] == None:
                        if tile.piece:
                            self.selected_tiles[0] = tile
                            tile.toggle_select()
                            log.log(str(tile) + " was selected")
                    elif self.selected_tiles[1] == None:
                        #Make sure the pieces are not the same team
                        if tile.piece:
                            if tile.piece.piece_type.value[1] != self.selected_tiles[0].piece.piece_type.value[1]:
                                self.selected_tiles[1] = tile
                                tile.toggle_select()
                        else:
                            self.selected_tiles[1] = tile
                            tile.toggle_select()
                    else:
                        self.selected_tiles[0].toggle_select()
                        self.selected_tiles[1].toggle_select()
                        self.selected_tiles[0] = None
                        self.selected_tiles[1] = None
                        if tile.piece:
                            self.selected_tiles[0] = tile
                            tile.toggle_select()

    def deselect_last(self):
        if self.selected_tiles[0] != None:
            self.selected_tiles[0].toggle_select()
        if self.selected_tiles[1] != None:
            self.selected_tiles[1].toggle_select()

    def __str__(self):
        row = ""
        for i in range(8):
            for j in range(7):
                row += str(self.tiles[i][j]) + ", "
            row += str(self.tiles[i][7]) + "\n"
        return row

