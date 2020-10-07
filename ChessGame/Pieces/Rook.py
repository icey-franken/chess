from . import Piece


class Rook(Piece.Piece):
    def __init__(self, color, is_captured=False, name='Rook'):
        super().__init__(color,  is_captured)
