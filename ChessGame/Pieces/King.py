from . import Piece


class King(Piece.Piece):
    def __init__(self, color, name='King', is_captured=False):
        super().__init__(color, is_captured)
