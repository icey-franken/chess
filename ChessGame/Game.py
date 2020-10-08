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
        player_1_name = input('Enter a name for player 1: ')
        player_2_name = input('Enter a name for player 2: ')

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
        name = self.white_player.name if self.turn == 'White' else self.black_player.name
        file_rank = '--'
        piece_pos = None
        piece = None
        while piece_pos is None or piece is None:
            file_rank = input(f'''Player {name}
            Enter a piece to move by file and rank: ''')
            piece_pos = self.board.translate_file_rank_to_col_row(file_rank)
            piece = self.board.is_valid_piece_selection(piece_pos, self.turn)

        move_file_rank = None

        valid_move_pos_list = self.board.get_valid_moves(piece_pos, self.turn)

        is_valid = False

        valid_file_ranks = [self.board.translate_col_row_to_file_rank(pos)
                            for pos in valid_move_pos_list]

        while is_valid is False:
            move_file_rank = input(f'''{name}'s turn
    Possible moves are: {valid_file_ranks}
    Enter the file and rank of where you want to move your {piece}.
    Piece currently at {file_rank}:
            ''')
            if move_file_rank in valid_file_ranks:
                is_valid = True
            else:
                print('That is not a valid move')
        print(move_file_rank)


        # square = self.board.get_square(move_pos)
        # print(square)

game = Game()
game.create_new_game()
# print(game.board)
game.start_turn_sequence()
