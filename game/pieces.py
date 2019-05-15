from enum import Enum
import pygame

class PieceType(Enum):
    #ENUM NAME      IMAGE SOURCE                            COLOR
    KING_BLACK =    ("icons/icons8-king-filled-50.png",     0)
    QUEEN_BLACK =   ("icons/icons8-queen-filled-50.png",    0)
    ROOK_BLACK =    ("icons/icons8-rook-filled-50.png",     0)
    KNIGHT_BLACK =  ("icons/icons8-knight-filled-50.png",   0)
    BISHOP_BLACK =  ("icons/icons8-bishop-filled-50.png",   0)
    PAWN_BLACK =    ("icons/icons8-pawn-filled-50.png",     0)

    KING_WHITE =    ("icons/icons8-king-50.png",            1)
    QUEEN_WHITE =   ("icons/icons8-queen-50.png",           1)
    ROOK_WHITE =    ("icons/icons8-rook-50.png",            1)
    KNIGHT_WHITE =  ("icons/icons8-knight-50.png",          1)
    BISHOP_WHITE =  ("icons/icons8-bishop-50.png",          1)
    PAWN_WHITE =    ("icons/icons8-pawn-50.png",            1) 

class Piece():
    def __init__(self, piece_type):
        self.piece_type = piece_type
        self.image_source = piece_type.value[0]
        self.image = pygame.image.load(self.image_source)

    def image_object(self):
        return self.image

    def __str__(self):
        return str(self.piece_type.name)

class King_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.KING_BLACK)
    
    def get_image(self):
        return self.image_object()

class Queen_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.QUEEN_BLACK)
    
    def get_image(self):
        return self.image_object()

class Rook_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.ROOK_BLACK)
    
    def get_image(self):
        return self.image_object()

class Knight_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.KNIGHT_BLACK)
    
    def get_image(self):
        return self.image_object()

class Bishop_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.BISHOP_BLACK)
    
    def get_image(self):
        return self.image_object()

class Pawn_Black(Piece):
    def __init__(self):
        super().__init__(PieceType.PAWN_BLACK)
    
    def get_image(self):
        return self.image_object()

class King_White(Piece):
    def __init__(self):
        super().__init__(PieceType.KING_WHITE)
    
    def get_image(self):
        return self.image_object()

class Queen_White(Piece):
    def __init__(self):
        super().__init__(PieceType.QUEEN_WHITE)
    
    def get_image(self):
        return self.image_object()

class Rook_White(Piece):
    def __init__(self):
        super().__init__(PieceType.ROOK_WHITE)
    
    def get_image(self):
        return self.image_object()

class Knight_White(Piece):
    def __init__(self):
        super().__init__(PieceType.KNIGHT_WHITE)
    
    def get_image(self):
        return self.image_object()

class Bishop_White(Piece):
    def __init__(self):
        super().__init__(PieceType.BISHOP_WHITE)
    
    def get_image(self):
        return self.image_object()

class Pawn_White(Piece):
    def __init__(self):
        super().__init__(PieceType.PAWN_WHITE)
    
    def get_image(self):
        return self.image_object()