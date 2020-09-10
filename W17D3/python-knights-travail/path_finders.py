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
        self._root = Node(startPos)
        self._posTuple = posTuple
        self._considered_positions = {startPos}

    @property
    def rootNode(self):
        return self._root

    @property
    def start(self):
        return self._root.value

    @property
    def pos(self):
        return self._posTuple

    @property
    def consideredMoves(self):
        return self._considered_positions

    def get_valid_moves(self, pos):
        validMovesList = []
        oneMoves = [1, -1]
        twoMoves = [2, -2]
        for move1 in oneMoves:
            xMove1 = move1 + pos[0]
            yMove1 = move1 + pos[1]
            for move2 in twoMoves:
                xMove2 = move2 + pos[0]
                yMove2 = move2 + pos[1]
                if 0 <= xMove1 < 9 and 0 <= yMove2 < 9:
                    validMovesList.append((xMove1, yMove2))
                if 0 <= xMove2 < 9 and 0 <= yMove1 < 9:
                    validMovesList.append((xMove2, yMove1))
        return set(validMovesList)

    def new_move_positions(self, pos):
        # grab all possible moves based on current position
        possibleMoves = self.get_valid_moves(pos)
        # use difference operator (-)
        # find which possible moves are NOT in considered moves
        newPossibleMoves = possibleMoves - self.consideredMoves
        # add each new possible move to considered moves
        for move in newPossibleMoves:
            self.consideredMoves.add(move)
        return newPossibleMoves

    def build_move_tree(self):
        node = self.rootNode  # to start
        # initialize positions array with start position
        positions = [self.start]
        while len(positions) > 0:
            # get all new move positions from first position entry
            moves = self.new_move_positions(positions[0])
            # moves is a set of all unique moves
            for move in moves:
                # create a node for each one and add as child to node
                childNode = Node(move)
                node.add_child(childNode)
                # print('new child node: ', childNode)
                # print('node after child added: ', node)
                # add the move to the positions list
                positions.append(move)
            # remove first position entry - all new moves added
            print(node)
            positions.remove(positions[0])
            # assign node last so we can initialize with root node
            # this is kind of defeating the pupose of a while loop
            # but without this check at the end it throws an error
            if len(positions) > 0:
                node = Node(positions[0])
        return self

    def find_path(self, end_position):
        endNode = self.rootNode.depth_search(end_position)
        return endNode

    def __str__(self):
        return('''path-finders.py
        start: {0}
        pos: {1}
        considered_positions: {2}'''
               .format(self.start, self.pos, self.consideredMoves))


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
rootImmediateChildren = finder.rootNode.children

print(rootImmediateChildren[0])
print(finder.find_path((3, 3)))
# logger.debug(finder)
# builtMoveTree = finder.build_move_tree()
# logger.debug(builtMoveTree)
# # logger.debug(builtMoveTree.rootNode.children[0])
# # logger.debug(finder.find_path((3, 3)))
# print(finder._root.children)
# # logger.debug(finder.rootNode.children[0])
# print('------------------------')
# these print like I expect - the issue is that they look wrong when printed from find path function
# logger.debug(finder.rootNode)
# logger.debug(finder.rootNode.children)
# logger.debug(finder.rootNode.children[0]) # .children[0])
# logger.debug(finder.rootNode.children[0].children[0].parent)
