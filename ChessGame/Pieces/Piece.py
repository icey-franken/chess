# each piece will inherit from this class.
# what will be unique to each individual piece is the valid_moves calculation
# I think everything else will be basically the same

# advantage of get_position method vs just accessing piece property?

class Piece:
    def __init__(self, position, color, name=None, is_captured=False):
        self.position = position
        self._color = color
        self.is_captured = is_captured

    def get_position(self):
        return self.position

    def __repr__(self):
        return f'{str(self._color)} {str(self._name)} {str(self.position)}'
