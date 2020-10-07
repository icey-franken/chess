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
    # eventually we can put a validation here that game is over/forfeited/whatever
    def white_pieces(self, white_pieces):
        self._white_pieces = white_pieces
        # return self.white_pieces()

    @property
    def black_pieces(self):
        return self._black_pieces

    @black_pieces.setter
    def black_pieces(self, black_pieces):
        self._black_pieces = black_pieces

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
            white_king=King((3, 0), 'White'),
            white_queen=Queen((4, 0), 'White'),
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
            black_king=King((3, 7), 'Black'),
            black_queen=Queen((4, 7), 'Black'),
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
        all_pieces = dict(**white_pieces, **black_pieces)
        # for piece in all_pieces.keys():
        #     logging.info(all_pieces[piece])
        # for piece in black_pieces.keys():
        #     logging.info(black_pieces[piece])
        # for piece in white_pieces.keys():
        #     logging.info(white_pieces[piece])

    def clear_board(self):
        pass

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
# logging.info(newBoard)
newBoard.add_pieces_for_new_game()
logging.info(newBoard.white_pieces)
# logging.info(newBoard.white_pieces['white_rook_1'].get_position())
sq = newBoard._squares[0][0]
dummyPiece = Pawn((0, 0), 'White')
logging.info(f'piece info: {dummyPiece}')
logging.info(f'square info: {sq}')
logging.info(f'square 0 0 occ: {sq.occupant}')
logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')

sq.occupant = dummyPiece
logging.info(f'square 0 0 occ: {sq.occupant}')
logging.info(f'square 0 0 is_occ: {sq.is_occupied()}')
