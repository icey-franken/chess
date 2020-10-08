from . import Piece


class Pawn(Piece.Piece):
    # def __init__(self, color,  is_captured=False):
    # super().__init__(color, is_captured)

    def get_valid_moves(self, position, board):
        """OLD - SAVED JUST IN CASE
            - this method takes in a position
            - when user clicks a square we check if it is their turn and the piece belongs to them based on square.occupant property
            square = self.get_square(position)
            piece = square.occupant
            if piece is None:
                print('this square is empty')
                return
            elif piece.color is not player.color:
                print('this is not your piece to move')
                return

            - if neither return is hit then this is a moveable piece
            - we now want to highlight available moves for player
            - first get list of sublists containing valid piece moves based on position and piece type
                - we assume here that piece knows nothing of position
            valid_piece_moves = piece.get_valid_piece_moves(position)
            - determine valid_board_moves using valid_piece_moves and board knowledge
                - for each sublist in valid_piece_moves we start at the beginning and go until space occupied - something like:

            valid_board_moves = []
            # this for loop accesses each sublist
            for i in range(len(valid_piece_moves)):
                sublist = valid_piece_moves[i]
                j = 0
                !!!make sure to access square based on position given in sublist
                x, y = sublist[j] # this should be a x, y tuple
                while not self.squares[x][y].is_occupied:
                    valid_board_moves.append(sublist[j])
                    j += 1
                - when it kicks out of while loop, that means square at that position is occupied
                - we need to check the occupant: access occupant with self.square[x][y].occupant - this returns the specific piece instance on that square. We can then access color
                - if color is different, that move is valid
                - later on we can add a check for if the piece is king to change check status
                - this will work just fine for knight class as long as we put each move in it's own sublist!
                if self.squares[x][y].occupant.color != piece.color:
                    valid_board_moves.append(sublist[j])
                    if self.square[x][y].occupant.name == 'King':
                        # change check status
                        pass
            # at end of looping we return the valid_board_moves list
            # based on this list we will highlight valid squares
            return valid_board_moves
        """
        valid_moves_list = []  # remember - this is a list of sublists for each direction
        # pawns only have one direction (without attacking diagonals) and therefore one sublist but we still need nested form

        if self.color is 'White':
            # if first move (i.e. row is 1) then max_count is 2 - otherwise it's 1
            max_count = 2 if position[1] == 1 else 1
            # moves straigt forward
            valid_moves_list += self._get_moves_in_dir(
                position, board, 0, 1, max_count=max_count, can_attack=False)

            valid_moves_list += self._get_moves_in_dir(
                position, board, 1, 1, max_count=1, can_attack=True, only_attack=True)

            valid_moves_list += self._get_moves_in_dir(
                position, board, -1, 1, max_count=1, can_attack=True, only_attack=True)

        else:
            max_count = 2 if position[1] == 6 else 1

            valid_moves_list += self._get_moves_in_dir(
                position, board, 0, -1, max_count=max_count, can_attack=False)

            valid_moves_list += self._get_moves_in_dir(
                position, board, 1, -1, max_count=1, can_attack=True, only_attack=True)

            valid_moves_list += self._get_moves_in_dir(
                position, board, -1, -1, max_count=1, can_attack=True, only_attack=True)

        return valid_moves_list

        # column, row = position
        # # valid_moves_sublist = []
        # start_row = 1
        # row_inc = 1
        # if self.color == 'Black':
        #     start_row = 6
        #     row_inc = -1
        # # pawns can always move one row if space open
        # next_row = row + row_inc
        # is_open = board.get_square((column, next_row)).is_open()
        # if next_row <= 7 and next_row >= 0 and is_open:
        #     valid_moves_list.append((column, next_row))
        #     # if first move, pawn can also move up two rows
        #     # we only do this check if first check satisfied
        #     # i.e. next row unoccupied
        #     next_row = row + 2 * row_inc
        #     is_open = board.get_square((column, next_row)).is_open()
        #     if start_row == row and is_open:
        #         valid_moves_list.append((column, next_row))
        # # valid_moves_list.append(valid_moves_sublist)
        # valid_moves_list += self._get_valid_attack_moves(position, board)
        # return valid_moves_list

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
