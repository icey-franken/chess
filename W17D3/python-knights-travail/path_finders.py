from tree import Node
###############################################################################
# configure logging - here we just log to the console
###############################################################################
import logging
logger = logging.Logger(__file__)
# set the level for this logger
logger.setLevel(logging.DEBUG)
# set the level for the (console) logging handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
# define a format string for logging output (removed %(asctime)s)
formatter = logging.Formatter("Line%(lineno) d[%(levelname)s]: %(message)s")
# attach the formatter to the handler
handler.setFormatter(formatter)
# and the handler to the logger
logger.addHandler(handler)
###############################################################################


class KnightPathFinder():
    def __init__(self, posTuple, startPos=(0, 0)):
        self._root = startPos
        self._posTuple = posTuple
        self._considered_positions = {startPos}

    @property
    def start(self):
        return self._root

    @property
    def pos(self):
        return self._posTuple

    @property
    def considered(self):
        return self._considered_positions

    def get_valid_moves(self, pos):
        validMovesList = []
        oneMoves = [1, -1]
        twoMoves = [2, -2]
        for move in oneMoves:
            xMove1 = move + pos[0]
            yMove1 = move + pos[1]
            for move in twoMoves:
                xMove2 = move + pos[0]
                yMove2 = move + pos[1]
                if 0 <= xMove1 < 9 and 0 <= yMove2 < 9:
                    validMovesList.append((xMove1, yMove2))
                if 0 <= xMove2 < 9 and 0 <= yMove1 < 9:
                    validMovesList.append((xMove2, yMove1))

        print(validMovesList)
        # newXpos = pos[0] + 1
        # newYpos = pos[1] + 2
        # print(newXpos)
        # validMoves =

    def __str__(self):
        return('''
        start: {0}
        pos: {1}
        considered_positions: {2}'''
        .format(self.start, self.pos, self.considered))


finder = KnightPathFinder((1, 2))
logger.debug(finder)
logger.debug(finder.get_valid_moves((8, 8)))
