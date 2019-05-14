from enum import Enum

class PieceType(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    KNIGHT = 4
    BISHOP = 5
    PAWN = 6

class Piece():
    def __init__(self, piece_type):
        self.piece_type = piece_type

    def __str__(self):
        return self.piece_type.name