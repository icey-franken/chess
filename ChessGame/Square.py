class Square:
    def __init__(self, x_pos, y_pos, occupant=None):
        self._pos = (x_pos, y_pos)
        self._is_white = self.get_color(x_pos, y_pos)
        self._occupant = occupant

    def get_color(self, x, y):
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
    def set_occupant(self, newOccupant):
        if self.is_occupied():
            return 'Space is occupied - fuck off'
        else:
            self._occupant = newOccupant

    def is_occupied(self):
        return self.occupant is not None

    def __str__(self):
        color = 'white'
        if self._is_white is False:
            color = 'black'
        return f'Pos: {self._pos}, Color: {color}'

    def __repr__(self):
        color = 'white'
        if self._is_white is False:
            color = 'black'
        return f'Pos: {self._pos}, Color: {color}'
