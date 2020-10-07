# Piece is a MODULE. To get the Piece class, we access Piece.Piece
from . import Piece


class Knight(Piece.Piece):
    def __init__(self, position, color, name='Knight', is_captured=False):
        super().__init__(position, color, is_captured)
        self._name = name
