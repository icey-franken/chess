from . import Piece


class Bishop(Piece.Piece):
    def __init__(self, color, name='Bishop', is_captured=False):
        super().__init__(color, is_captured)
