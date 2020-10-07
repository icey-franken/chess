from . import Piece


class Queen(Piece.Piece):
    def __init__(self, color, name='Queen', is_captured=False):
        super().__init__(color, is_captured)
