class Piece:
    def __init__(self, position, color, is_captured=False):
        self.position = position
        self._color = color
        self.is_captured = is_captured
