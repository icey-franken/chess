from Square import Square
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn


# There's gotta be a better way to do imports
# from Pieces import (
#     Pawn,
#     Rook,
#     Bishop,
#     Knight,
#     King,
#     Queen
# )
# Pawn = Pawn.Pawn
# Rook = Rook.Rook
# Bishop = Bishop.Bishop
# Knight = Knight.Knight
# King = King.King
# Queen = Queen.Queen


class Board:
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8']

    def __init__(self):
        self._squares = []
        self._white_pieces = None
        self._black_pieces = None

    def create_board(self):
        new_squares = []
        for y in range(8):
            column = []
            for x in range(8):
                square = Square(y, x)
                column.append(square)
            new_squares.append(column)
        self.squares = new_squares

    @property
    def squares(self):
        return self._squares

    @squares.setter
    def squares(self, new_squares):
        self._squares = new_squares

    def get_square(self, position):
        x, y = position  # position is a tuple of x, y coords
        return self.squares[x][y]

    @property
    def white_pieces(self):
        return self._white_pieces

    @white_pieces.setter
    # eventually we can put a validation here that game is over/forfeited
    def white_pieces(self, white_pieces):
        self._white_pieces = white_pieces
        # return self.white_pieces()

    @property
    def black_pieces(self):
        return self._black_pieces

    @black_pieces.setter
    def black_pieces(self, black_pieces):
        self._black_pieces = black_pieces

    # on second thought - we don't want to delete pieces!
    # instead we want to change their is_captured attribute!
    # @black_pieces.deleter
    # def black_pieces(self, removed_piece):
    #     print(removed_piece)
    #     if removed_piece in self.black_pieces:
    #         del self._black_pieces[removed_piece]
    #     else:
    #         print('piece not in black_pieces')

    def translate_file_rank_to_col_row(self, file_rank):
        '''rank_file should be a string like a1, b5, h8, etc.
        - files are letters, ranks are numbers
        - this method turns it to a col, row tuple
        - allows access to square in self.squares
        '''
        file = file_rank[0]
        if file not in self.files:
            print('Invalid file')
            return
        col = self.files.index(file)

        rank = file_rank[1]
        if rank not in self.ranks:
            print('Invalid rank')
            return
        row = self.ranks.index(rank)
        return (col, row)

    def translate_col_row_to_file_rank(self, pos):
        col, row = pos
        file = self.files[col]
        rank = self.ranks[row]
        return f'{file}{rank}'

    def create_pieces_for_new_game(self):
        """
        instantiates class object for each piece type
        sets piece in corresponding start position
        white occupies rows 1 and 2
        black occupies rows 7 and 8
        """
        # maybe we don't even want to do this - what we really want to do is assign pieces as occupants of corresponding squares

        # Haven't decided if a piece needs to know about position - for now we include but I may remove in the future

        white_pieces = dict(
            white_rook_1=Rook('White'),
            white_knight_1=Knight('White'),
            white_bishop_1=Bishop('White'),
            white_queen=Queen('White'),
            white_king=King('White'),
            white_bishop_2=Bishop('White'),
            white_knight_2=Knight('White'),
            white_rook_2=Rook('White'),
            white_pawn_1=Pawn('White'),
            white_pawn_2=Pawn('White'),
            white_pawn_3=Pawn('White'),
            white_pawn_4=Pawn('White'),
            white_pawn_5=Pawn('White'),
            white_pawn_6=Pawn('White'),
            white_pawn_7=Pawn('White'),
            white_pawn_8=Pawn('White'),
        )

        black_pieces = dict(
            black_rook_1=Rook('Black'),
            black_knight_1=Knight('Black'),
            black_bishop_1=Bishop('Black'),
            black_queen=Queen('Black'),
            black_king=King('Black'),
            black_bishop_2=Bishop('Black'),
            black_knight_2=Knight('Black'),
            black_rook_2=Rook('Black'),
            black_pawn_1=Pawn('Black'),
            black_pawn_2=Pawn('Black'),
            black_pawn_3=Pawn('Black'),
            black_pawn_4=Pawn('Black'),
            black_pawn_5=Pawn('Black'),
            black_pawn_6=Pawn('Black'),
            black_pawn_7=Pawn('Black'),
            black_pawn_8=Pawn('Black'),
        )
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces
        # ** is called 'splat' - similar to spread in JS
        # all_pieces = dict(**white_pieces, **black_pieces)
        # for piece in all_pieces.keys():
        #     logging.info(all_pieces[piece])
        # for piece in black_pieces.keys():
        #     logging.info(black_pieces[piece])
        # for piece in white_pieces.keys():
        #     logging.info(white_pieces[piece])

    def set_pieces_for_new_game(self):
        squares = self.squares
        whites = self.white_pieces
        blacks = self.black_pieces
        squares[0][0].occupant = whites['white_rook_1']
        squares[1][0].occupant = whites['white_knight_1']
        squares[2][0].occupant = whites['white_bishop_1']
        squares[3][0].occupant = whites['white_queen']
        squares[4][0].occupant = whites['white_king']
        squares[5][0].occupant = whites['white_bishop_2']
        squares[6][0].occupant = whites['white_knight_2']
        squares[7][0].occupant = whites['white_rook_2']

        squares[0][1].occupant = whites['white_pawn_1']
        squares[1][1].occupant = whites['white_pawn_2']
        squares[2][1].occupant = whites['white_pawn_3']
        squares[3][1].occupant = whites['white_pawn_4']
        squares[4][1].occupant = whites['white_pawn_5']
        squares[5][1].occupant = whites['white_pawn_6']
        squares[6][1].occupant = whites['white_pawn_7']
        squares[7][1].occupant = whites['white_pawn_8']

        squares[0][7].occupant = blacks['black_rook_1']
        squares[1][7].occupant = blacks['black_knight_1']
        squares[2][7].occupant = blacks['black_bishop_1']
        squares[3][7].occupant = blacks['black_queen']
        squares[4][7].occupant = blacks['black_king']
        squares[5][7].occupant = blacks['black_bishop_2']
        squares[6][7].occupant = blacks['black_knight_2']
        squares[7][7].occupant = blacks['black_rook_2']

        squares[0][6].occupant = blacks['black_pawn_1']
        squares[1][6].occupant = blacks['black_pawn_2']
        squares[2][6].occupant = blacks['black_pawn_3']
        squares[3][6].occupant = blacks['black_pawn_4']
        squares[4][6].occupant = blacks['black_pawn_5']
        squares[5][6].occupant = blacks['black_pawn_6']
        squares[6][6].occupant = blacks['black_pawn_7']
        squares[7][6].occupant = blacks['black_pawn_8']

    # def uncapture_all_pieces_for_new_game(self):
        # pass

    def clear_board(self):
        squares = self.squares
        for i in range(len(squares)):
            column = squares[i]
            for j in range(len(column)):
                column[j].occupant = None

    def on_board(self, position):
        column, row = position
        return (column >= 0 and column <= 7 and row >= 0 and row <= 7)

    def is_valid_piece_selection(self, position, player_color):
        '''this method returns none if a square is empty
        or if the piece does not belong to the current player.
        Otherwise it returns the valid piece.
        '''
        if position is None:
            return
        square = self.get_square(position)
        piece = square.occupant
        if piece is None:
            print('That space is empty')
            return
        elif piece.color != player_color:
            print('That is not your piece')
            return
        else:
            return piece

    def get_valid_moves(self, position, player_color):
        """
        This method simply determines if a piece is a player's to move based on position and color.
        If it is, then it calls the piece's get_valid_moves method and returns moves.
        Otherwise it returns none.
        """
        piece = self.is_valid_piece_selection(position, player_color)
        if piece is not None:
            return piece.get_valid_moves(position, self)

    def move_piece(self, piece_pos, move_pos):
        '''This method returns None if piece moved to open space,
        or returns captured piece if space occupied by opponent piece'''
        piece_square = self.get_square(piece_pos)
        piece = piece_square.occupant
        piece_square.occupant = None
        move_square = self.get_square(move_pos)
        captured_piece = None
        if move_square.is_occupied():
            captured_piece = move_square.occupant
            move_square.occupant = None
            captured_piece.is_captured = True
        move_square.occupant = piece
        return captured_piece

    def get_king_pos(self, color):
        for i in range(len(self.squares)):
            row = self.squares[i]
            for j in range(len(row)):
                square = row[j]
                piece = square.occupant
                if piece is None:
                    continue
                elif piece.name == 'King' and piece.color == color:
                    return square.pos

    def king_in_check(self, player_color, king_pos = None):
        # king_position if necessary because if player is moving the king, we need to calculate check based on where king WILL be, not where it currently is
        # if piece is NOT king, then this check serves to make sure that king is not currently in check.

# FOR MAKING SURE THAT PLAYER TAKES CARE OF OWN KING
        # added is_in_check property to player class
        #   first we move the piece, but save previous "state"
        #       in either case (check or not) we check if in check after piece move
        #           if in check is true after piece move, rewind to before piece moved and prompt user that they can't put their king in check (if not in check before) or that their king still in check - try again (if in check before)
                    # else if not in check after piece move, all is well - proceed.

# NEED TO ADD FORMULA TO CHECK IF  MOVE PUTS OPPONENT KING IN CHECK
        #   if king is currently in check, we move the piece first and then check if king still in check
        #       if king remains in check, we undo the piece move
        #       if king no longer in check, we proceed
        #   if king is NOT currently in check,
        # get the position of king for whatever input color was
        # I know there are much more efficient ways to figure this out - but for now I will iterate through all squares and grab those with occupant.name of King
        oppo_color = 'Black' if player_color == 'White' else 'White'

        if king_pos is None:
            king_pos = self.get_king_pos(player_color)

        if king_pos is None:
            print('error in king_in_check method in board.py line 291')
        # we should have position of player's king
        # now for ALL opponent pieces we need to see if that position if in valid_moves
        # if so return True
        oppo_moves_to_get_king = []  # maybe fill this out later
        king_in_check = False
        for i in range(len(self.squares)):
            row = self.squares[i]
            for j in range(len(row)):
                square = row[j]
                piece = square.occupant
                if piece is None:
                    continue
                else:
                    if piece.color == oppo_color:
                        # this is an opponents piece - get valid moves
                        oppo_piece_moves = self.get_valid_moves(square.pos, oppo_color)
                        if king_pos in oppo_piece_moves:
                            king_in_check = True
                            return king_in_check  # return here because we dont need to keep looping
        return king_in_check  # should always be false if it hit's here
        # then check if that king's position is in the list returned from get_valid_moves for the opposing color
        # if so return true
        # otherwise return false

    def __repr__(self):

        startRowStr = '''
       a          b          c          d          e          f          g          h
  _________________________________________________________________________________________'''
        endRowStr = '''
       a          b          c          d          e          f          g          h     '''

        def make_row(x, row_num):
            row = f'''
  |          |          |          |          |          |          |          |          |
  |          |          |          |          |          |          |          |          |
{row_num} |    {x[0]}    |    {x[1]}    |    {x[2]}    |    {x[3]}    |    {x[4]}    |    {x[5]}    |    {x[6]}    |    {x[7]}    | {row_num}
  |          |          |          |          |          |          |          |          |
  |__________|__________|__________|__________|__________|__________|__________|__________|'''
            return row

        rowStr = ''
        transposed_board = [[], [], [], [], [], [], [], []]
        for i in range(len(self.squares)):
            row = self.squares[i]
            for j in range(len(row)):
                col_item = '--' if row[j].occupant is None else row[j].occupant
                transposed_board[j].append(col_item)
                # col.append(col_item)
        for i in range(len(transposed_board), 0, -1):
            row = transposed_board[i-1]
            occupants = [row[j] for j in range(len(row))]
            rowStr += make_row(occupants, i)
        return startRowStr+rowStr+endRowStr


    #################################################################
# newBoard = Board()
# newBoard.make_board()
# newBoard.create_pieces_for_new_game()
# newBoard.set_pieces_for_new_game()
# logging.info(newBoard)
# position = (1, 0)
# square = newBoard.get_square(position)
# piece = square.occupant
# logging.info(f'square: {square} piece: {piece}')
# # logging.info(f'piece name: {piece.name}')
# # logging.info(
#     # f'valid piece moves: {piece.get_valid_moves(position, newBoard)}')
# logging.info(
#     f'valid board moves: {newBoard.get_valid_moves(position)}')

# print(piece.name)
# print(piece.color)

# logging.info(newBoard.squares)
# newBoard.clear_board()
# logging.info(newBoard.squares)

# logging.info(newBoard.white_pieces)
# whiteKingStartPos = newBoard.white_pieces['white_king'].get_position()
# blackKingStartPos = newBoard.black_pieces['black_king'].get_position()
