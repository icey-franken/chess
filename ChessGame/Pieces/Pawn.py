from . import Piece


class Pawn(Piece.Piece):
    def __init__(self, color,  is_captured=False, name='Pawn'):
        super().__init__(color, is_captured, name)

    def get_valid_piece_moves(self, position):
        # for pawns, color matters - white can only move "up" and black can only move "down"
        # valid piece moves assume board is empty - purely piece logic
        # for white pawns, if row is 1 then it has not moved - can move 'up' 1 or 2 rows
        # for black pawns same deal but row 6 and down
        # pawns can only change columns if there is a piece - this will be more complex logic to implement later
        #
        valid_moves_list = []  # remember - this is a list of sublists for each direction
        # pawns only have one direction (without attacking diagonals) and therefore one sublist but we still need nested form
        column, row = position
        # we assume for all operations that current column and row are valid (i.e. between 0 and 7)
        valid_moves_sublist = []
        if self.color == 'White':
            # white pawns can always move up one row (assuming that row is on board)
            if row + 1 <= 7:
                valid_moves_sublist.append((column, row + 1))
            if row == 1:
                # if first move, pawn can also move up two rows - don't need to check <= 7
                valid_moves_sublist.append((column, row + 2))
        elif self.color == 'Black':
            # black pawns can always move down one row
            if row - 1 >= 0:
                valid_moves_sublist.append((column, row - 1))
            if row == 6:
                valid_moves_sublist.append((column, row - 2))
        valid_moves_list.append(valid_moves_sublist);
        return valid_moves_list
