from . import Piece


class King(Piece.Piece):
    def __init__(self, position, color, name='King', is_captured=False):
        super().__init__(position, color, is_captured)
        self._name = name
