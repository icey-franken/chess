class Square:
    # class variables defined before __init__ ('constructor')
    # access with self.x_files OR Square.x_files OR self.__class__.x_files
    # I think self.__class__ is the most pythonic?
    x_files = 'abcdefgh'
    y_ranks = '12345678'

    def __init__(self, x_pos, y_pos, occupant=None):
        self._pos = (x_pos, y_pos)
        self._is_black = self.determine_is_black(x_pos, y_pos)
        self._occupant = occupant
        self._name = self.get_square_name_from_pos()

    # no reason to have setter/deleter for square position - will never change
    @property
    def pos(self):
        return self._pos

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     name = self.get_square_name_from_pos()
    #     self._name = name

    def get_square_name_from_pos(self):
        x_pos, y_pos = self.pos
        x_file = self.__class__.x_files[x_pos]
        y_rank = self.__class__.y_ranks[y_pos]
        return x_file + y_rank

    # def get_square_pos_from_name(self, name):
    #     x_file = name[0]

    #     y_rank = name[1]



    # getter method for square color
    @property
    def is_black(self):
        return self._is_black

    # setter method for square color
    # @is_black.setter
    # def set_is_black(self, is_black):
    #     self._is_black = is_black

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

    # occupant will be an instance of a piece on which we can call various methods
    @occupant.setter
    def occupant(self, newOccupant):
        if self.is_occupied() and newOccupant is not None:
            print('SPOT IS OCCUPIED - MOVE NOT MADE')
        elif not self.is_occupied() and newOccupant is None:
            print('SPOT IS ALREADY EMPTY')
        else:
            self._occupant = newOccupant

    # I don't think we need a deleter - instead we want to set newOccupant to None
    # @occupant.deleter
    # def occupant(self):
    #     if not self.is_occupied():
    #         print('NO PIECE IN THIS SQUARE - PIECE NOT DELETED')
    #     else:
    #         self._occupant = None

    def is_occupied(self):
        return self.occupant is not None





    def __str__(self):
        color = 'White' if self.is_black is False else 'Black'
        return f'Pos: {self._pos}, Color: {color}'

    def __repr__(self):
        color = 'White' if self.is_black is False else 'Black'
        return f'Pos: {self._pos}, Color: {color}'
