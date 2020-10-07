class Square:
    def __init__(self, x_pos, y_pos, occupant=None):
        self._pos = (x_pos, y_pos)
        self._is_black = self.determine_is_black(x_pos, y_pos)
        self._occupant = occupant

    # getter method for square color
    @property
    def is_black(self):
        return self._is_black

    # setter method for square color
    @is_black.setter
    def set_is_black(self, is_black):
        self._is_black = is_black

    # determines if square is black or not based on square position
    # method called in square constructor upon instantiation
    def determine_is_black(self, x, y):
        if x % 2 == 0 and y % 2 == 0:
            return True
        elif x % 2 != 0 and y % 2 != 0:
            return True
        else:
            return False


    @property
    def occupant(self):
        return self._occupant

    @occupant.setter
    def occupant(self, newOccupant):
        if self.is_occupied():
            print('SPOT IS OCCUPIED - MOVE NOT MADE')
        else:
            self._occupant = newOccupant

    @occupant.deleter
    def occupant(self):
        self._occupant = None

    def is_occupied(self):
        return self.occupant is not None





    def __str__(self):
        color = 'White' if self.is_black is False else 'Black'
        return f'Pos: {self._pos}, Color: {color}'

    def __repr__(self):
        color = 'White' if self.is_black is False else 'Black'
        return f'Pos: {self._pos}, Color: {color}'
