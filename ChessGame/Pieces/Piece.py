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
    def __init__(self, color, is_captured=False):  # , name=None):
        # self._position = position
        self._color = color
        self._is_captured = is_captured
        self._name = self.__class__.__name__

        # self._name = name

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

    def _get_moves_in_dir(self, position, board, col_inc, row_inc, max_count=7):
        """
        This method calculates all moves in a straight line
        col_inc and row_inc should be +1, 0, or -1 for rook, knight, bishop, and queen
        straight lines with only one of col_inc or row_inc non-zero
        diagonal lines with both non-zero
        for king we can calculate moves with max_count = 1

        """
        moves_list = []
        column, row = position
        next_col = column + col_inc
        next_row = row + row_inc
        next_pos = (next_col, next_row)
        count = 0
        while board.on_board(next_pos) and count < max_count:
            # next_pos = (next_col, row)
            # if next square is empty then move valid
            square = board.get_square(next_pos)
            if square.is_open():
                moves_list.append(next_pos)
            else:
                if square.occupant.color != self.color:
                    moves_list.append(next_pos)
                break
            next_col += col_inc
            next_row += row_inc
            next_pos = (next_col, next_row)
            count += 1
        return moves_list

    # @property
    # def position(self):
    #     return self._position

    # @position.setter
    # def position(self, newPosition):
    #     """
    #     -here we can set "validations"
    #     -  make sure that desired position is on the board
    #     -also makes sense to check that space not occupied
    #     -  I think that's a board operation
    #     -  or at least for something "above" the piece class
    #     -newPosition is a tuple - values must be between 0 and 7
    #     """
    #     x_pos, y_pos = newPosition
    #     if x_pos < 0 or x_pos > 7:
    #         print('x position (rank?) out of range')
    #     elif y_pos < 0 or y_pos > 7:
    #         print('y position (file?) out of range')
    #     else:
    #         self._position = newPosition

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
        cap_str = 'CAPTURED' if self.is_captured else 'NOT captured'
        return f'[{self.color} {self.name}-{cap_str}]'
