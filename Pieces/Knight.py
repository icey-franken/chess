# Piece is a MODULE. To get the Piece class, we access Piece.Piece
from . import Piece


class Knight(Piece):
    # we define knight_move_incs here and not on piece
    #   - only knight cares about these
    knight_move_incs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def get_valid_moves(self, position, board):
        valid_moves_list = []
        for col_inc, row_inc in self.knight_move_incs:
            moves = self._get_moves_in_dir(position, board, col_inc,
                                           row_inc, max_count=1)
            valid_moves_list += moves
        return valid_moves_list
