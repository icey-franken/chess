from Square import Square
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn
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
    def __init__(self):
        self._squares = []
        self._white_pieces = None
        self._black_pieces = None

    def make_board(self):
        new_squares = []
        for x in range(8):
            column = []
            for y in range(8):
                square = Square(x, y)
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

        squares[1][3].occupant = blacks['black_rook_1']
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
        return column >= 0 and column <=7 and row >= 0 and row <= 7

    def get_valid_board_moves(self, position):
        """
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
        # need to define player class - use default of white for now
        player_color = 'White'
        square = self.get_square(position)
        piece = square.occupant
        if piece is None:
            print('this square is empty')
            return
        elif piece.color is not player_color:
            print('this is not your piece to move')
            return
        valid_piece_moves = piece.get_valid_piece_moves(position, self)
        return valid_piece_moves


    def __repr__(self):
        boardStr = ''
        endStr = '''
 |________________________________________
     a    b    c    d    e    f    g    h  '''
        for i in range(len(self._squares)-1, -1, -1):
            rowStr = f''' |
{i+1}| '''
            row = self._squares[i]
            for j in range(len(row)):
                square = row[j]
                color = 'W'
                if square.is_black:
                    color = 'B'
                rowStr += f'  {color}  '
            boardStr += f'''
{rowStr}'''
        return boardStr + endStr


#####################################################################
newBoard = Board()
newBoard.make_board()
logging.info(newBoard)
newBoard.create_pieces_for_new_game()
newBoard.set_pieces_for_new_game()
position = (1, 1)
square = newBoard.get_square(position)
logging.info(f'white pawn square: {square}')
piece = square.occupant
logging.info(f'square 0 1 piece: {piece}')
# logging.info(f'piece name: {piece.name}')
logging.info(f'valid piece moves: {piece.get_valid_piece_moves(position, newBoard)}')
logging.info(f'valid board moves: {newBoard.get_valid_board_moves(position)}')

print(piece.name)
print(piece.color)



# logging.info(newBoard.squares)
# newBoard.clear_board()
# logging.info(newBoard.squares)

# logging.info(newBoard.white_pieces)
# whiteKingStartPos = newBoard.white_pieces['white_king'].get_position()
# blackKingStartPos = newBoard.black_pieces['black_king'].get_position()


# logging.info(whiteKingStartPos)
# logging.info(newBoard.white_pieces['white_king'].get_square_name_from_pos())
# whiteKingSq = newBoard._squares[whiteKingStartPos[0]][whiteKingStartPos[1]]
# logging.info(
# f'white king square name: {whiteKingSq.get_square_name_from_pos()}')
# blackKingSq = newBoard._squares[blackKingStartPos[0]][blackKingStartPos[1]]
# logging.info(
# f'black king square name: {blackKingSq.get_square_name_from_pos()}')

# sq = newBoard._squares[0][0]
# logging.info(f'board coords {sq.get_square_name_from_pos()}')
# dummyPiece = Pawn((0, 0), 'White')
# logging.info(f'piece info: {dummyPiece}')
# logging.info(f'square info: {sq}')
# logging.info(f'square 0 0 occ: {sq.occupant}')
# logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')

# sq.occupant = dummyPiece
# logging.info(f'square 0 0 occ: {sq.occupant}')
# logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')
# if sq.is_occupied():
#     logging.info(sq.occupant)
#     sq.occupant = None
#     logging.info(sq.occupant)


"""
TO MAKE A MOVE:
- assume that move is valid for particular piece - will add method
    - "valid move" depends on piece type and position
        - position must be within the board
        - position must be of piece's ability
        - position must be unoccupied or occupied by opposing piece
        - SPECIAL CASE FOR KINGS - WORRY LATER
- if move valid (again ONLY based on piece type and position):
    - if Square.is_occupied() is False: move piece
        - "moving piece": set occupant in square; change piece position
    - elif Square.is_occupied() is True: check occupant
        - if occupant is same color, move is invalid - DON'T MOVE
        - if occupant is diff color, move is valid
            - change current occupant is_captured to True
            - move piece: set occupant in square, change piece position.

- I should add a method on each piece type that will return all potential moves based ONLY on piece type and current position
    - this is because piece has no knowledge of other pieces on the board
- the board will filter out invalid moves based on if current occupant color for each valid move matches the piece to be moved
- the result of this filtering are ACTUALLY valid moves
- only distinction from that point is if a piece will be caputred or not.


**thought: the valid moves thing needs to be completely on a piece, so maybe a piece needs to know about the squares on board class.
I say this because valid moves is different for each piece. For example, most pieces can only move until they reach another piece - they can't move beyond that. But knights dpon't care about that.
I can either pass the board into each get_valid_moves for each piece, OR I can put a special case on the board class for piece name is knight - in that case we get rid of thing that stops piece movement if it encounters another piece.
"""
