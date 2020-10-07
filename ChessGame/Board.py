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
        for x in range(8):
            row = []
            for y in range(8):
                square = Square(x, y)
                row.append(square)
            self._squares.append(row)

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

    def add_pieces_for_new_game(self):
        """
        instantiates class object for each piece type
        sets piece in corresponding start position
        white occupies rows 1 and 2
        black occupies rows 7 and 8
        """
        white_pieces = dict(
            white_rook_1=Rook((0, 0), 'White'),
            white_knight_1=Knight((1, 0), 'White'),
            white_bishop_1=Bishop((2, 0), 'White'),
            white_queen=Queen((3, 0), 'White'),
            white_king=King((4, 0), 'White'),
            white_bishop_2=Bishop((5, 0), 'White'),
            white_knight_2=Knight((6, 0), 'White'),
            white_rook_2=Rook((7, 0), 'White'),
            white_pawn_1=Pawn((0, 1), 'White'),
            white_pawn_2=Pawn((1, 1), 'White'),
            white_pawn_3=Pawn((2, 1), 'White'),
            white_pawn_4=Pawn((3, 1), 'White'),
            white_pawn_5=Pawn((4, 1), 'White'),
            white_pawn_6=Pawn((5, 1), 'White'),
            white_pawn_7=Pawn((6, 1), 'White'),
            white_pawn_8=Pawn((7, 1), 'White'),
        )

        black_pieces = dict(
            black_rook_1=Rook((0, 7), 'Black'),
            black_knight_1=Knight((1, 7), 'Black'),
            black_bishop_1=Bishop((2, 7), 'Black'),
            black_queen=Queen((3, 7), 'Black'),
            black_king=King((4, 7), 'Black'),
            black_bishop_2=Bishop((5, 7), 'Black'),
            black_knight_2=Knight((6, 7), 'Black'),
            black_rook_2=Rook((7, 7), 'Black'),
            black_pawn_1=Pawn((0, 6), 'Black'),
            black_pawn_2=Pawn((1, 6), 'Black'),
            black_pawn_3=Pawn((2, 6), 'Black'),
            black_pawn_4=Pawn((3, 6), 'Black'),
            black_pawn_5=Pawn((4, 6), 'Black'),
            black_pawn_6=Pawn((5, 6), 'Black'),
            black_pawn_7=Pawn((6, 6), 'Black'),
            black_pawn_8=Pawn((7, 6), 'Black'),
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

    def clear_board(self):
        pass

    def get_valid_board_moves(self, piece_to_move):
        """
        - this method takes in a particular piece
        - we access Piece.color to determine if we get piece from self.white_pieces or self.black_pieces
            - maybe it makes more sence to have all pieces in one spot - for now don't worry
        - we access piece_to_move to get that piece instance

        - assuming that piece_to_move is something like "white_rook_1" and that we put all pieces together:
        piece = self.all_pieces[piece_to_move]
        - on the piece we have position, color, is_captured, and name. On piece type we have get_valid_piece_moves method:
            - this method accesses position on piece to calculate valid moved
        valid_piece_moves = piece.get_valid_piece_moves()
        - valid_piece_moves should be a list of sublists

        - for each sublist we start at the beginning and go until space occupied - something like:
            valid_board_moves = []
            # this accesses each sublist
            for i in range(len(valid_piece_moves)):
                sublist = valid_piece_moves[i]
                j = 0
                !!!make sure to access square based on position given in sublist
                x, y = sublist[j] # this should be a x, y tuple
                while not self.squares[x][y].is_occupied:
                    valid_board_moves.append(sublist[j])
                    j += 1

        - ***SEE BELOW: based on get_piece_moves return value, the board then checks squares at those positions and filters moves
            - if is_occupied and occupant color is the same as current piece then that move is invalid
            -


        - I think for each Piece type we want a method that returns possible moves in a list of sublists (with no board knowledge).
            - each sublist is possible moves going in one direction, starting from piece position to the end of the board
            - in that way if we find that a space is occupied midway through the sublist we can slice the list at that point and remove moves beyond.
            - we can do that operation on each sublist (for all but knight piece)
            - end result will be possible moves
        """



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
newBoard.add_pieces_for_new_game()
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

sq = newBoard._squares[0][0]
logging.info(f'board coords {sq.get_square_name_from_pos()}')
dummyPiece = Pawn((0, 0), 'White')
logging.info(f'piece info: {dummyPiece}')
logging.info(f'square info: {sq}')
logging.info(f'square 0 0 occ: {sq.occupant}')
logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')

sq.occupant = dummyPiece
logging.info(f'square 0 0 occ: {sq.occupant}')
logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')
if sq.is_occupied():
    logging.info(sq.occupant)
    sq.occupant = None
    logging.info(sq.occupant)


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
