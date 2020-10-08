from . import Piece


class King(Piece.Piece):
    def get_valid_moves(self, position, board):
        valid_moves_list = []
        for col_inc, row_inc in self.all_move_incs:
            moves = self._get_moves_in_dir(position, board, col_inc, row_inc, max_count=1)
            valid_moves_list += moves
        return valid_moves_list
