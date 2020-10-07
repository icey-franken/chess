# each piece will inherit from this class.
# what will be unique to each individual piece is the valid_moves calculation
# I think everything else will be basically the same

# advantage of get_position method vs just accessing piece property?

# - I think for each Piece type we want a method that returns possible moves in a list of sublists (with no board knowledge - only position knowledge).
#             - each sublist is possible moves going in one direction, starting from piece position to the end of the board
#             - in that way if we find that a space is occupied midway through the sublist we can slice the list at that point and remove moves beyond.
#             - we can do that operation on each sublist (for all but knight piece)
#             - end result will be possible moves

class Piece:
    def __init__(self, position, color, name=None, is_captured=False):
        self._position = position
        self._color = color
        self._is_captured = is_captured
        self._name = name

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, newPosition):
        """
        -here we can set "validations"
        -  make sure that desired position is on the board
        -also makes sense to check that space not occupied
        -  I think that's a board operation
        -  or at least for something "above" the piece class
        -newPosition is a tuple - values must be between 0 and 7
        """
        x_pos, y_pos = newPosition
        if x_pos < 0 or x_pos > 7:
            print('x position (rank?) out of range')
        elif y_pos < 0 or y_pos > 7:
            print('y position (file?) out of range')
        else:
            self._position = newPosition

    @property
    def is_captured(self):
        return self._is_captured

    @is_captured.setter
    def is_captured(self, captured_boolean):
        if(self.is_captured == captured_boolean):
            if self.is_captured is True:
                print('Piece is already captured!')
            elif self.is_captured is False:
                print('Piece is already ... not captured!')
        else:
            self._is_captured = captured_boolean




    def __repr__(self):
        return f'{str(self._color)} {str(self._name)} {str(self.position)}'
