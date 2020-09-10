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


class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):  # getter for node value
        return self._value

    @property
    def children(self):  # getter for node children list
        return self._children

    # @children.setter
    def add_child(self, child):  # setter for add child to node
        if child not in self.children:
            self.children.append(child)
        if child.parent is not self:
            # child.parent(self)  # this
            child.parent = self  # or this

    # @children.setter
    def remove_child(self, child):  # setter for remove node's child
        if child in self.children:
            self.children.remove(child)
        if child.parent is not None:
            # child.parent(None)  # this
            child.parent = None  # or this

    @staticmethod
    def killchildren():
        pass

    # def set_age(self, age):
    #     self._age = age

    # def get_age(self):
    #     return self._age
    # age = property(set_age, get_age, None, 'this is the age property')

    @property
    def parent(self):  # getter for node's parent
        return self._parent

    @parent.setter
    def parent(self, newParent):  # setter for node's parent
        oldParent = self.parent
        if self.parent is not newParent:
            self._parent = newParent
        if oldParent is not None and oldParent != newParent:
            self._parent = None
            oldParent.remove_child(self)  # this
            # oldParent.remove_child = self  # or this
        if newParent is not None:
            newParent.add_child(self)  # this
            # newParent.add_child = self  # or this

        # if newParent is None:
        #     self._parent = None

        # print(self.parent is not None)

        # if self.parent is not None:
            # parent.add_child(parent())

    def __str__(self):
        return('{0} (parent: {1}) children: {2}'
               .format(self.value,
                       self.parent and self.parent.value,
                       [child.value for child in self.children]))
        #  %
        #        (self.value,
        #         self.parent and self.parent.value,
        #         ', '.join([child.value for child in list(self.children)])))

######################################################
# in class: we need to tell pyton what it means for a node equality looks like.
# In our case, we want the value to be the same (I think).
    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        else:
            return self.value == other.value

    ######################################################
    # depth first search of nodes - method
    #  returns node that contains the value if it exists, else return None
    # @staticmethod
    # this is an iterative method - I think the test wants a recursive method
    # def depth_search(self, value):
    #     searchList = [self]
    #     while len(searchList) > 0:
    #         currentNode = searchList[0]
    #         # logger.debug(currentNode)
    #         if currentNode.value == value:
    #             return currentNode
    #         currentNode.children.reverse()
    #         for child in currentNode.children:
    #             searchList.insert(0, child)
    #         searchList.remove(currentNode)
    #     return None

    # recursive depth_search method
    def depth_search(self, value):
        if self.value == value:
            return self
        for child in self.children:
            result = child.depth_search(value)
            if result is not None:
                return result

    ######################################################

    # breadth first search of nodes - method
    #  returns node that contains the value if it exists, else return None
    # @staticmethod
    def breadth_search(self, value):
        searchList = [self]
        while len(searchList) > 0:
            currentNode = searchList[0]
            if currentNode.value == value:
                return currentNode
            for child in currentNode.children:
                searchList.append(child)
            searchList.remove(currentNode)
        return None


####################################################
# Gordon said this was a way to test that our code is doing what we want it to.
if __name__ == '__main__':
    class TreeNodeIsSearchable:
        def setUp(self):
            self.nodes = [Node(i) for i in "abcdefg"]
            parent_index = 0
            for index, child in enumerate(self.nodes):
                if index == 0:
                    continue
                child.parent = self.nodes[parent_index]
                parent_index += 1 if index % 2 == 0 else 0
            return self.nodes
        # node = Node('George')
        # node.add_child(Node('Mary'))
        # node.add_child(Node('David'))
        # logger.debug(node)
    nodes = TreeNodeIsSearchable().setUp()
    logger.debug([nodes[i].value for i in range(len(nodes))])
    logger.debug(nodes[0].depth_search('e'))
    logger.debug(nodes[4])
    # logger.debug(type(nodes))
    # print(node)


########################################################
#  practice/scratch code
########################################################

node1 = Node('root1')
node2 = Node('root2')
node3 = Node('root3')
# print('node1.value ', node1.value)
# print('node1.children before ', node1.children)
# node1.add_child = node2
# print('node1.children after ', node1.children)

node3.parent = node1
node3.parent = node2

# print(node1.children)
# print(node2.children)
# child1 = Node('child1')
# parent1 = Node('parent')
# child2 = Node('child2')
# child3 = Node('child3')


# child1.parent = parent1
# child2.parent = parent1
