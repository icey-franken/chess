# each piece will inherit from this class.
# what will be unique to each individual piece is the valid_moves calculation

class Piece:
    # move_incs here will be used by queen, king, bishop, rook
    # knight class defines it's own move_inc list
    # pawn class has no list - hard-coded instead
    diag_move_incs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    straight_move_incs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    all_move_incs = [*diag_move_incs, *straight_move_incs]

    def __init__(self, color, is_captured=False):
        self._color = color
        self._is_captured = is_captured
        self._name = self.__class__.__name__

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

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

    def _get_moves_in_dir(self, position, board, col_inc, row_inc,
                          max_count=7, can_attack=True,
                          only_attack=False):
        """
            Method calculates all moves extending out from position by col/row_inc
            - col/row_inc is +1, 0, or -1 for rook, knight, bishop, and queen
            - straight lines with only one of col/row_inc non-zero
            - diagonal lines with both non-zero
            - for king we can calculate moves with max_count = 1
            - can_attack property is primarily for pawns
                - pawns cannot attack moving straight up and down.
                - For all others can_attack = True is correct
            - I may be doing too much with this function
                - maybe it would be better to have a couple different functions
                - just something to consider - for now this is ok
            - each specific piece implements this function differently
        """
        moves_list = []
        col, row = position
        next_col = col + col_inc
        next_row = row + row_inc
        next_pos = (next_col, next_row)
        count = 0
        # check that move on board and count not exceeded
        while board.on_board(next_pos) and count < max_count:
            # if so, get the board square
            square = board.get_square(next_pos)
            # if the square is open, add the move to that square
            # only_attack is special case for pawns
            #   - can ONLY move to diag. square if it is occupied
            if not only_attack and square.is_open():
                moves_list.append(next_pos)
            else:
                # if square is occupied by opposing piece, add that move
                # can_attack again is special case for pawns
                #   - pawn forward moves CANNOT attack - unique
                if can_attack and square.occupant.color != self.color:
                    moves_list.append(next_pos)
                # in any case, after first occupied square we break
                break
            # increment col/row; increment count
            next_col += col_inc
            next_row += row_inc
            next_pos = (next_col, next_row)
            count += 1
        return moves_list

    def __str__(self):
        color_str = 'W' if self.color == 'White' else 'B'
        piece_str = self.name[0] if self.name != 'King' else '*'
        return f'{color_str}{piece_str}'

    def __repr__(self):
        cap_str = 'CAPTURED' if self.is_captured else 'NOT captured'
        return f'[{self.color} {self.name}-{cap_str}]'
