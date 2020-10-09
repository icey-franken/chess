class Player():
    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._is_in_check = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, player_name):
        self._name = player_name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, player_color):
        if player_color == 'White' or player_color == 'Black':
            self._color = player_color
        else:
            print('That is not a valid color')

    @property
    def is_in_check(self):
        return self._is_in_check

    @is_in_check.setter
    def is_in_check(self, in_check):
        self._is_in_check = in_check

    def __repr__(self):
        return f'<{self.name} - {self.color} pieces>'
