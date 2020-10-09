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

    def get_valid_pos_and_piece_from_player(self):
        # initialize variables to be used in while loop
        # file_rank = '--'
        piece_pos = None
        piece = None
        # valid_move_pos_list = None
         # this while loop runs until player selects a piece that:
        #   - is their's
        #   - has at least one move
        while piece is None:
            # prompt player to enter a square
            file_rank = input(f'''Player {player.name}
    Enter a piece to move by file and rank: ''')

            # turn file rank to col row
            #   - if invalid the method will print what was wrong
            #   - method will return None => loop continues
            piece_pos = self.board.translate_file_rank_to_col_row(file_rank)
            # get piece vased on piece_pos
            #   - if user input of file_rank is not valid, piece also returns None
            #   - if user inputs valid file_rank but they don't have a piece there, piece is None and error is printed
            piece = self.board.is_valid_piece_selection(piece_pos, self.turn)

            # piece will only be not None if valid file rank and valid piece selection return successfully - if not, hits else and continues.
            #   IMPROVEMENT: instead, we can just say if piece is None => continue - user then prompted to enter a file_rank again

            # if piece is None:
                # continue
            # now we don't need an else statment, and less nesting.
            # function only gets to this point if piece not None

            # this was initially calling get_valid_moves on board class.
            #   that method checks that piece exists and belongs to player before calling get_valid_moves.
            #   we already called is_valid_piece_selection above, so we know piece is valid.
            #   therefore we call method on piece itself
            # if no moves for that piece, we want to start this while loop again

        return piece_pos, piece

    def move_pos_list_to_file_ranks(self, valid_move_pos_list):
        # turn each col row tuple into a file rank format
        valid_file_ranks = [self.board.translate_col_row_to_file_rank(pos)
                            for pos in valid_move_pos_list]
        # make a single string of possible moves
        valid_file_ranks_str = ''
        for file_rank_option in valid_file_ranks:
            valid_file_ranks_str += file_rank_option + ' '
        return valid_file_ranks, valid_file_ranks_str



    def get_valid_piece_move_from_player(self, valid_move_pos_list):
        ### printing valid moves in nice format for player
        valid_file_ranks, valid_file_ranks_str = self.move_pos_list_to_file_ranks(valid_move_pos_list)

        move_file_rank = None
        while True:
            # prompt user to select a space to move piece to
            # tell user piece name, position, and possible moves.
            move_file_rank = input(f'''{player.name}'s turn
    Enter the file and rank of where you want to move your {piece.name}.
        Piece currently at: {file_rank}
        Possible moves are: {valid_file_ranks_str}
        Selected move: ''')
        # if true - move is valid (unless problem with king in check)
            if move_file_rank in valid_file_ranks:
                move_pos = self.board.translate_file_rank_to_col_row(move_file_rank)

                # subfunction here to check for .. check

                # check that self not put in check with selected move
                # logging.info(self.board.king_in_check(player.color, ))
                king_pos = move_pos if piece.name == 'King' else None
                if self.board.king_in_check(player.color, king_pos=king_pos):
                    print('''    You cannot put your own King in check - try again.
                    ''')
                    piece = None
                    break
                # move_piece method moves piece at piece_pos to move_pos
                # if space was previously occupied it returns the captured piece;
                # otherwise it returns none
                captured_piece = self.board.move_piece(piece_pos, move_pos)
                if captured_piece is not None:
                    print(f'''    You captured {opponent.name}\'s {captured_piece.name}''')
                # before we finish player's turn, we check if the opponents king is in check
                if self.board.king_in_check(opponent.color):
                    print(f'''    Heads up {opponent.name}! Your King is in check.
        You next move must get your King out of check or you LOSE.''')
                break
            else:
                print('''That is not a valid move - try again.
                ''')
        continue






    def play_turn_sequence(self):
        print(self.board)
        # determine the player and opponent based on self.turn
        player = self.white_player
        opponent = self.black_player
        if self.turn == 'Black':
            player = self.black_player
            opponent = self.white_player

        #########################
        #getting valid piece selection from player
        # prompt user to enter valid piece
        piece_pos, piece = self.get_valid_pos_and_piece_from_player()
        # get valid moves for piece
        valid_move_pos_list = piece.get_valid_moves(piece_pos, self.board)
        # if first selection no good, enter while loop
        # alerts user that no moves available, then repeats above functions
        while len(valid_move_pos_list) == 0:
            print('No available moves for that piece.')
            piece_pos, piece = self.get_valid_pos_and_piece_from_player()
            valid_move_pos_list = piece.get_valid_moves(piece_pos, self.board)

       ########################
        # getting valid piece move from player
        # at this point we know they selected a valid, moveable piece
        # if not they'd be stuck in above while loop
        # you cannot unselect a piece - "chess rules"
        self.get_valid_piece_move_from_player(valid_move_pos_list)

        ###

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
            self.play_turn_sequence()



        # square = self.board.get_square(move_pos)
        # print(square)

game = Game()
game.create_new_game()
# print(game.board)
game.play_turn_sequence()
