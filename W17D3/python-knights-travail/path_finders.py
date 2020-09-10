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
        boardSize = 9  # change to 9 - 4 for debugging purposes
        validMovesList = []
        oneMoves = [1, -1]
        twoMoves = [2, -2]
        for move1 in oneMoves:
            xMove1 = move1 + pos[0]
            yMove1 = move1 + pos[1]
            for move2 in twoMoves:
                xMove2 = move2 + pos[0]
                yMove2 = move2 + pos[1]
                if 0 <= xMove1 < boardSize and 0 <= yMove2 < boardSize:
                    validMovesList.append((xMove1, yMove2))
                if 0 <= xMove2 < boardSize and 0 <= yMove1 < boardSize:
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
        # initialize positions array with root node
        nodes = [self.rootNode]
        while len(nodes) > 0:
            parentNode = nodes.pop(0)
            # get all new move positions first position entry
            # moves is a set of all unique moves
            moves = self.new_move_positions(parentNode.value)
            for move in moves:
                # create a node for each one and add as child to node
                childNode = Node(move)
                parentNode.add_child(childNode)
                # add the NODE to the positions list
                # problem I had was because I was creating new nodes every time
                nodes.append(childNode)

    def find_path(self, end_position):
        endNode = self.rootNode.breadth_search(end_position)
        path = self.trace_to_root(endNode)
        return path

    def trace_to_root(self, end_node):
        nodeList = [end_node]
        node = end_node
        # print(node.parent, node.parent is None)
        # print(node.parent.parent, node.parent.parent is None)
        while node.parent is not None:
            # print(node, node.parent)
            node = node.parent
            nodeList.append(node)
        nodeList.reverse()
        positionList = [node.value for node in nodeList]
        return positionList

    def __str__(self):
        return('''path-finders.py
        start: {0}
        pos: {1}
        considered_positions: {2}'''
               .format(self.start, self.pos, self.consideredMoves))


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print('find path for (2, 1): ', finder.find_path((2, 1)))
print('find path for (3, 3): ', finder.find_path((3, 3)))
print('find path for (6, 2): ', finder.find_path((6, 2)))
print('find path for (7, 6): ', finder.find_path((7, 6)))

# print('find path for (8,8): ', finder.find_path((4, 7)))
# logger.debug(finder)
# builtMoveTree = finder.build_move_tree()
# logger.debug(builtMoveTree)
# # logger.debug(builtMoveTree.rootNode.children[0])
# # logger.debug(finder.find_path((3, 3)))
# print(finder._root.children)
# # logger.debug(finder.rootNode.children[0])
# print('------------------------')
# these print like I expect - the issue is that they look wrong when printed find path function
# logger.debug(finder.rootNode)
# logger.debug(finder.rootNode.children)
# logger.debug(finder.rootNode.children[0]) # .children[0])
# logger.debug(finder.rootNode.children[0].children[0].parent)
