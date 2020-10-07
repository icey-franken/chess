from . import Piece


class Rook(Piece.Piece):
    def __init__(self, position, color, is_captured=False, name='Rook'):
        super().__init__(position, color,  is_captured, name,)
        self._name = name
