from Board import Board
from Player import Player
from copy import deepcopy
import logging

FORMAT = '[%(filename)s:%(lineno)d] %(message)s'
LEVEL = logging.INFO
logger = logging.getLogger(__name__)
logging.basicConfig(format=FORMAT, level=LEVEL)

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
        '''this method creates board, creates pieces, sets pieces on board, and gets player names and colors'''
        self.board = Board()
        self.board.create_board()
        self.board.create_pieces_for_new_game()
        self.board.set_pieces_for_new_game()
        self.get_player_names_and_colors()

    def get_player_names_and_colors(self):
        '''this method prompts players to enter names and choose colors. It then creates new player instances and assigns them to the game class'''
        player_1_name = input('Enter a name for player 1: ').title()
        player_2_name = input('Enter a name for player 2: ').title()

        white_player_number = None
        while white_player_number not in ['1', '2']:
            white_player_number = input(
                'Which player wants to use white pieces? Enter 1 or 2: ')
        if white_player_number == '1':
            self.white_player = Player(player_1_name, 'White')
            self.black_player = Player(player_2_name, 'Black')
        else:
            self.black_player = Player(player_1_name, 'Black')
            self.white_player = Player(player_2_name, 'White')
        print(f'''
                    {self.white_player} vs {self.black_player}''')

    def get_valid_pos_and_piece_from_player(self, player_name):
        '''this method does what it frickin says'''
        piece_file_rank = piece_pos = piece = None
        # this while loop runs until player selects a piece that:
        #   - is their's
        #   - has at least one move
        while piece is None:
            # prompt player to enter a square
            piece_file_rank = input(f'''Player {player_name}
        Enter a piece to move by file and rank: ''')
            # turn file rank to col row
            #   if invalid then method prints error, returns None
            piece_pos = self.board.translate_file_rank_to_col_row(
                piece_file_rank)
            # get piece based on piece_pos
            #   if invalid then method prints error, returns None
            piece = self.board.is_valid_piece_selection(piece_pos, self.turn)
        # return the following to be used in play_turn_sequence
        return piece_file_rank, piece_pos, piece

    def move_pos_list_to_file_ranks(self, valid_move_pos_list):
        '''this method takes in valid_move_pos_list.
        Returns them all converted to file_rank format.
        Also returns a string of all file ranks to be printed to user.
        '''
        # turn each col row tuple into a file rank format
        valid_file_ranks = [self.board.translate_col_row_to_file_rank(pos)
                            for pos in valid_move_pos_list]
        # make a single string of possible moves
        valid_file_ranks_str = ''
        for file_rank_option in valid_file_ranks:
            valid_file_ranks_str += file_rank_option + ' '
        return valid_file_ranks, valid_file_ranks_str

    def get_valid_piece_move_from_player(self, player, opponent,
                                         piece_name, piece_file_rank,
                                         piece_pos, move_pos_list):
        '''this method '''
        file_ranks, file_ranks_str = self.move_pos_list_to_file_ranks(
            move_pos_list)
        move_file_rank = None
        # prompt user to select a space to move piece to
        # tell user piece name, position, and possible moves.
        move_file_rank = input(f'''{player.name}'s turn
        Enter the file and rank of where you want to move your {piece_name}.
            Piece currently at: {piece_file_rank}
            Possible moves are: {file_ranks_str}
            Selected move: ''')
        # if true then invalid move input
        # return false so that play_turn_sequence while loop restarts
        # gives user chance to select diff piece and try again
        if move_file_rank not in file_ranks:
            print('That is not a valid move.')
            return False
        # file rank to col row
        move_pos = self.board.translate_file_rank_to_col_row(
            move_file_rank)

        # simulate making the move using copy of board
        board_copy = deepcopy(self.board)
        # save captured_piece for later in case move valid
        captured_piece = board_copy.move_piece(piece_pos, move_pos)
        # check if king in check on simulated board
        king_put_in_check = board_copy.king_in_check(player.color)
        # if in check - return False so play_turn_sequence loop restarts
        if king_put_in_check:
            print('''    You cannot put your own King in check - try again.
            ''')
            return False
        # if king not put in check, then move is good
        # reassign real board to simulated board since all good
        self.board = board_copy
        print('Move successful.')
        if captured_piece is not None:
            print(
                f'''    You captured {opponent.name}\'s {captured_piece.name}''')
        # check if opponent's king in check before we finish player's turn
        if self.board.king_in_check(opponent.color):
            print(f'''
        Heads up {opponent.name}! Your King is in check.
            You next move must get your King out of check or you LOSE.
        ''')
        # return true to indicate that move made successfully, for now
        return True

    def play_turn_sequence(self):
        print(self.board)
        # determine the player and opponent based on self.turn
        player = self.white_player
        opponent = self.black_player
        if self.turn == 'Black':
            player = self.black_player
            opponent = self.white_player

        # we remain in this loop in the case of check
        # then, at any point in this loop we can say "continue" and user will be prompted to select a different piece
        while True:
            #########################
            # getting valid piece selection from player
            # prompt user to enter valid piece
            piece_file_rank, piece_pos, piece = self.get_valid_pos_and_piece_from_player(
                player.name)
            # get valid moves for piece
            valid_move_pos_list = piece.get_valid_moves(piece_pos, self.board)
            # if first selection no good, enter while loop
            # alerts user that no moves available, then repeats above functions
            while len(valid_move_pos_list) == 0:
                print('No available moves for that piece.')
                piece_file_rank, piece_pos, piece = self.get_valid_pos_and_piece_from_player(
                    player.name)
                valid_move_pos_list = piece.get_valid_moves(
                    piece_pos, self.board)

        ########################
            # getting valid piece move from player
            # if move invalid, we return false and while loop continues
            # otherwise we break out of loop and finish turn
            if self.get_valid_piece_move_from_player(
                player, opponent, piece.name, piece_file_rank, piece_pos, valid_move_pos_list):
                break
        # at this point move has been made successfully - we want to change self.turn and call play_turn_sequence method again
        self.finish_turn()
        # check for check mate - if true, call game over method
        if self._game_over:
            pass
            # return self.game_over()
            # do something to end game, display winner, etc
        else:
            self.play_turn_sequence()



game = Game()
game.create_new_game()
game.play_turn_sequence()
