from . import Piece


class Rook(Piece.Piece):
    def get_valid_moves(self, position, board):
        valid_moves_list = []
        for col_inc, row_inc in self.straight_move_incs:
            moves = self._get_moves_in_dir(position, board, col_inc, row_inc)
            valid_moves_list += moves
        return valid_moves_list
