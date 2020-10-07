from . import Piece


class Bishop(Piece.Piece):
    def __init__(self, position, color, name='Bishop', is_captured=False):
        super().__init__(position, color, is_captured)
        self._name = name
