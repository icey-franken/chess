from . import Piece


class Queen(Piece):
    def get_valid_moves(self, position, board):
        valid_moves_list = []
        for col_inc, row_inc in self.all_move_incs:
            moves = self._get_moves_in_dir(position, board, col_inc, row_inc)
            valid_moves_list += moves
        return valid_moves_list


# def _get_moves_in_row(self, position, board, row_inc):
#     row_moves_list = []
#     column, row = position
#     next_row = row + row_inc
#     while next_row <= 7 and next_row >= 0:
#         next_pos = (column, next_row)
#         # if next square is empty then move valid
#         square = board.get_square(next_pos)
#         if square.is_open():
#             row_moves_list.append(next_pos)
#         else:
#             if square.occupant.color != self.color:
#                 row_moves_list.append(next_pos)
#             break
#         next_row += row_inc
#     return row_moves_list

# def _get_moves_in_col(self, position, board, col_inc):
#     col_moves_list = []
#     column, row = position
#     next_col = column + col_inc
#     while next_col <= 7 and next_col >= 0:
#         next_pos = (next_col, row)
#         # if next square is empty then move valid
#         square = board.get_square(next_pos)
#         if square.is_open():
#             col_moves_list.append(next_pos)
#         else:
#             if square.occupant.color != self.color:
#                 col_moves_list.append(next_pos)
#             break
#         next_col += col_inc
#     return col_moves_list


    # def _get_moves_in_dir(self, position, board, col_inc, row_inc):
    #     moves_list = []
    #     column, row = position
    #     next_col = column + col_inc
    #     next_row = row + row_inc
    #     next_pos = (next_col, next_row)
    #     while board.on_board(next_pos):
    #         # next_pos = (next_col, row)
    #         # if next square is empty then move valid
    #         square = board.get_square(next_pos)
    #         if square.is_open():
    #             moves_list.append(next_pos)
    #         else:
    #             if square.occupant.color != self.color:
    #                 moves_list.append(next_pos)
    #             break
    #         next_col += col_inc
    #         next_row += row_inc
    #         next_pos = (next_col, next_row)
    #     return moves_list

        #  and board.get_square((column, next_row)).is_occupied
        # for i in range(len(valid_piece_moves)):
        #     sublist = valid_piece_moves[i]
        #     for j in range(len(sublist)):
        #         x, y = sublist[j]
        #         square = self.squares[x][y]
        #         # if square is empty, then that's a valid move
        #         if not square.is_occupied():
        #             valid_board_moves.append(sublist[j])
        #         else:
        #             # if a square is occupied and its a different color, we want to add that move and then break
        #             # EXCEPT if the piece is a pawn, because pawns can only attack diagonally
        #             if square.occupant.color != piece.color and piece.name != 'Pawn':
        #                 valid_board_moves.append(sublist[j])
        #                 # we know that square is occupied by piece of opposite color - we want to check if that piece is a king, and if so add a "player_in_check=True" or something property
        #                 if square.occupant.name == 'King':
        #                     # change check status
        #                     pass
        #             break  # in either case we want to break out of the sublist for loop after we hit the first occupied space
        # return valid_moves_list
