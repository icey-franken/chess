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
        # print('1child - child not in self.children' ,child not in self.children)
        if child not in self.children:
            self.children.append(child)
        # print('2child - child.parent is not self', child.parent is not self)
        # child.parent = self
        # changed parent method
        if child.parent is not self:
        #     # child.parent(self)  # this
            child.parent = self  # or this

        # print('3child - parent (self) at end of add child method', self)

    # @children.setter
    def remove_child(self, child):  # setter for remove node's child
        if child in self.children:
            self.children.remove(child)
            child.parent = None
        # changed parent method
        # if child.parent is not None:
        #     # child.parent(None)  # this
        #     child.parent = None  # or this

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
        # self._parent = newParent
        # print('''hits parent setter
        # self: {0}
        # parent: {1}
        # '''.format(self, newParent))
        # old code - changed so that you MUST call add/remove child. Do NOT set parent without calling one of those methods.
        # oldParent = self.parent
        # print(self.parent is not newParent)
        if self.parent is newParent:
            return
        if self.parent is not None:
            self.parent.remove_child(self)

        if newParent is not None:
            self._parent = newParent
            self.parent.add_child(self)
        else:
            self._parent = None
            # oldParent.remove_child = self  # or this
        # if newParent is not None:
        #     if self not in newParent.children:
        #         newParent.add_child(self)  # this
            # newParent.add_child = self  # or this
        # print('1parent - child (self) at end of parent setter', self)

        # if newParent is None:
        #     self._parent = None

        # print(self.parent is not None)

        # if self.parent is not None:
        # parent.add_child(parent())

    def __str__(self):
        return('''~~~tree.py value: {0} ---parent: {1} ---children: {2}~~~'''
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
        # print('value: ', value)
        # print('self: ', self)
        if self.value == value:
            return self
        for child in self.children:
            result = child.depth_search(value)
            if result is not None:
                return result
        return None
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
# if __name__ == '__main__':
#     class TreeNodeIsSearchable:
#         def setUp(self):
#             self.nodes = [Node(i) for i in "abcdefg"]
#             parent_index = 0
#             for index, child in enumerate(self.nodes):
#                 if index == 0:
#                     continue
#                 child.parent = self.nodes[parent_index]
#                 parent_index += 1 if index % 2 == 0 else 0
#             return self.nodes
#         # node = Node('George')
#         # node.add_child(Node('Mary'))
#         # node.add_child(Node('David'))
#         # logger.debug(node)
#     nodes = TreeNodeIsSearchable().setUp()
#     logger.debug([nodes[i].value for i in range(len(nodes))])
#     logger.debug(nodes[0].depth_search('e'))
#     logger.debug(nodes[4])
#     # logger.debug(type(nodes))
#     # print(node)


########################################################
#  practice/scratch code
########################################################

# node1 = Node('root1')
# node2 = Node('root2')
# node3 = Node('root3')
# # print('node1.value ', node1.value)
# # print('node1.children before ', node1.children)
# # node1.add_child = node2
# # print('node1.children after ', node1.children)

# node3.parent = node1
# node3.parent = node2

# # print(node1.children)
# # print(node2.children)
# # child1 = Node('child1')
# # parent1 = Node('parent')
# # child2 = Node('child2')
# # child3 = Node('child3')


# # child1.parent = parent1
# # child2.parent = parent1
