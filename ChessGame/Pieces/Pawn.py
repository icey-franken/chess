from . import Piece


class Pawn(Piece.Piece):
    def __init__(self, color,  is_captured=False, name='Pawn'):
        super().__init__(color, is_captured, name)
