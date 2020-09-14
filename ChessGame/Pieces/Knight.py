from Pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, position, color):
        # print(position)
        Piece.__init__(self, position, color)
        self._name = 'Knight'

    # def get_position(self):
    #     print(self, self.position)
    #     return self.position
