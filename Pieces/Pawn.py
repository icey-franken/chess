from . import Piece


class Pawn(Piece.Piece):

    def get_valid_moves(self, position, board):
        valid_moves_list = []

        if self.color is 'White':
            # if first move (i.e. row is 1) then max_count is 2 - otherwise 1
            max_count = 2 if position[1] == 1 else 1
            # moves straigt forward
            valid_moves_list += self._get_moves_in_dir(
                position, board, 0, 1, max_count=max_count, can_attack=False)
            # diagonal moves - attacking ONLY
            valid_moves_list += self._get_moves_in_dir(
                position, board, 1, 1, max_count=1,
                can_attack=True, only_attack=True)

            valid_moves_list += self._get_moves_in_dir(
                position, board, -1, 1, max_count=1,
                can_attack=True, only_attack=True)

        else:
            max_count = 2 if position[1] == 6 else 1

            valid_moves_list += self._get_moves_in_dir(
                position, board, 0, -1, max_count=max_count,
                can_attack=False)

            valid_moves_list += self._get_moves_in_dir(
                position, board, 1, -1, max_count=1,
                can_attack=True, only_attack=True)

            valid_moves_list += self._get_moves_in_dir(
                position, board, -1, -1, max_count=1,
                can_attack=True, only_attack=True)

        return valid_moves_list
