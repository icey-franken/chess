from Board import Board
from Player import Player
import logging
logger = logging.getLogger(__name__)
# formatter = logging.Formatter('{%(pathname)s:%(lineno)d}')
FORMAT = '[%(filename)s:%(lineno)d] %(message)s'
# FORMAT = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
# DATEFMT = '%Y-%m-%d:%H:%M:%S'
LEVEL = logging.INFO

logging.basicConfig(format=FORMAT, level=LEVEL)

# logger = logging.getLogger(__name__)
# logger.debug("This is a debug log")
# logger.info("This is an info log")
# logger.critical("This is critical")
# logger.error("An error occurred")

class Game():
    def __init__(self):
        self._turn = 'White'
        self.white_player = None
        self.black_player = None
        self._board = None
        self._game_over = False

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_board):
        self._board = new_board

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, next_turn):
        self._turn = next_turn

    def finish_turn(self):
        self.turn = 'Black' if self.turn == 'White' else 'White'

    def create_new_game(self):
        '''this method should create and set a new board
        - should prompt users for player names
        - prompt users for color choice
        - initiate the game
        '''
        self.board = Board()
        self.board.create_board()
        self.board.create_pieces_for_new_game()
        self.board.set_pieces_for_new_game()
        player_1_name = input('Enter a name for player 1: ').title()
        player_2_name = input('Enter a name for player 2: ').title()

        white_player_number = None
        while white_player_number not in ['1','2']:
            white_player_number = input('Which player wants to use white pieces? Enter 1 or 2: ')
        if white_player_number == '1':
            self.white_player = Player(player_1_name, 'White')
            self.black_player = Player(player_2_name, 'Black')
        else:
            self.black_player = Player(player_1_name, 'Black')
            self.white_player = Player(player_2_name, 'White')
        print(f'''
                    {self.white_player} vs {self.black_player}''')

    def start_turn_sequence(self):
        print(self.board)
        player_name = self.white_player.name
        opponent_name = self.black_player.name
        if self.turn == 'Black':
            player_name = self.black_player.name
            opponent_name = self.white_player.name
        file_rank = '--'
        piece_pos = None
        piece = None
        valid_move_pos_list = None
        while piece_pos is None or piece is None:
            file_rank = input(f'''Player {player_name}
    Enter a piece to move by file and rank: ''')
            piece_pos = self.board.translate_file_rank_to_col_row(file_rank)
            piece = self.board.is_valid_piece_selection(piece_pos, self.turn)
            if piece is not None:
                valid_move_pos_list = self.board.get_valid_moves(piece_pos, self.turn)
                if len(valid_move_pos_list) == 0:
                    piece = None
                    print('No available moves for that piece.')
        move_file_rank = None
        is_valid = False
        valid_file_ranks = [self.board.translate_col_row_to_file_rank(pos)
                            for pos in valid_move_pos_list]
        valid_file_ranks_str = ''
        for file_rank_opt in valid_file_ranks:
            valid_file_ranks_str += file_rank_opt + ' '
        while is_valid is False:
            move_file_rank = input(f'''{player_name}'s turn
    Enter the file and rank of where you want to move your {piece.name}.
        Piece currently at: {file_rank}
        Possible moves are: {valid_file_ranks_str}
        Selected move: ''')
            if move_file_rank in valid_file_ranks:
                is_valid = True
                # move piece
                move_pos = self.board.translate_file_rank_to_col_row(move_file_rank)
                captured_piece = self.board.move_piece(piece_pos, move_pos)
                if captured_piece is not None:
                    print(f'''    You captured {opponent_name}\'s {captured_piece.name}''')

            else:
                print('''That is not a valid move - try again
                ''')
        # after every time a piece is moved, we need to check that moved piece's valid moves
        # if we check after every successful piece move, we will never miss it
        # variable move_pos holds the current position of the piece that was just moved.
        # make a method on board class called king_put_in_check -
        #   this method will call get_valid_moves for the piece that just moved
        #   this method will also locate the opponents king position
        #   if the kings position is in valid_moves, then king_put_in_check should return True.

        # king_in_check - returns boolean if king in check or not
        #   if a selected move puts player's king in check - move not allowed
        #   if a selected move puts opponents king in check - opponent is alerted
        #     opponent must select a move that moves king out of check
        #       if for all valid moves of all opponent's remaining pieces the king is still in check, then check_mate - game over




        # if any of that piece's valid moves includes the opponent's king, we need to tell the opponent that they are in check
        # we need to save all moves that result in capturing the king
        # we need to make sure that the opponents next move takes the king out of check
        # if none of those moves exists - CHECK MATE!
        self.finish_turn()
        if self._game_over:
            pass
            # do something to end game, display winner, etc
        else:
            self.start_turn_sequence()



        # square = self.board.get_square(move_pos)
        # print(square)

game = Game()
game.create_new_game()
# print(game.board)
game.start_turn_sequence()
