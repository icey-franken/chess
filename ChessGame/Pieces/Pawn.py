from . import Piece


class Pawn(Piece.Piece):
    def __init__(self, position, color, name='Pawn', is_captured=False):
        super().__init__(position, color, is_captured)
        self._name = name
