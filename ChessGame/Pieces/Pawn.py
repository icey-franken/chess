from . import Piece


class Pawn(Piece.Piece):
    # def __init__(self, color,  is_captured=False):
    # super().__init__(color, is_captured)

    def get_valid_piece_moves(self, position, board):
        # for pawns, color matters - white can only move "up" and black can only move "down"
        # valid piece moves assume board is empty - purely piece logic
        # for white pawns, if row is 1 then it has not moved - can move 'up' 1 or 2 rows
        # for black pawns same deal but row 6 and down
        # pawns can only change columns if there is a piece - this will be more complex logic to implement later
        #
        valid_moves_list = []  # remember - this is a list of sublists for each direction
        # pawns only have one direction (without attacking diagonals) and therefore one sublist but we still need nested form
        column, row = position
        # valid_moves_sublist = []
        start_row = 1
        row_inc = 1
        if self.color == 'Black':
            start_row = 6
            row_inc = -1
        # pawns can always move one row if space open
        next_row = row + row_inc
        is_open = not board.get_square((column, next_row)).is_occupied()
        if next_row <= 7 and next_row >= 0 and is_open:
            valid_moves_list.append((column, next_row))
            # if first move, pawn can also move up two rows
            # we only do this check if first check satisfied
            # i.e. next row unoccupied
            next_row = row + 2 * row_inc
            is_open = not board.get_square((column, next_row)).is_occupied()
            if start_row == row and is_open:
                valid_moves_list.append((column, next_row))
        # valid_moves_list.append(valid_moves_sublist)
        valid_moves_list += self._get_valid_attack_moves(position, board)
        return valid_moves_list

    def _get_valid_attack_moves(self, position, board):
        valid_attacks = []
        row_inc = 1 if self.color == 'White' else -1
        column, row = position
        adj_row = row + row_inc
        left_atk = (column - 1, adj_row)
        right_atk = (column + 1, adj_row)
        if board.on_board(left_atk):
            left_square = board.get_square(left_atk)
            if left_square.is_occupied() and left_square.occupant.color != self.color:
                valid_attacks.append(left_atk)
        if board.on_board(right_atk):
            right_square = board.get_square(right_atk)
            if right_square.is_occupied() and right_square.occupant.color != self.color:
                valid_attacks.append(right_atk)
        return valid_attacks
