from Square import Square
# There's a better way to do this with destructuring but
from Pieces.Knight import Knight
# from Pieces.Rook import Rook
# from Pieces.Bishop import Bishop
# from Pieces.King import King
# from Pieces.Queen import Queen
# from Pieces.Pawn import Pawn


class Board:
    def __init__(self,):
        self._squares = []

    def make_board(self):
        for x in range(8):
            row = []
            for y in range(8):
                square = Square(x, y)
                row.append(square)
            self._squares.append(row)

    def add_pieces(self):
        '''calls piece for each piece, square.sets_oppucant for each relevant piece'''
        knight = Knight((0, 1), 'White')
        print('name', knight._name)
        print('position', knight.position)
        print('is captured', knight.is_captured)
        print('whole thing', knight)
        pass

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
                color = 'B'
                if square._is_white:
                    color = 'W'
                rowStr += f'  {color}  '
            boardStr += f'''
{rowStr}'''
        return boardStr + endStr


newBoard = Board()
newBoard.make_board()
print(newBoard)
newBoard.add_pieces()
