class Node():
    '''
    '''

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


class BST():
    '''
    '''

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert_value(self, value, current_node=False):
        ''' '''
        # TODO: Implement node value insertion method
        insertedNode = Node(value)

        if current_node is False and self._root is None:
            self._root = insertedNode
            return value
        elif current_node is False:
            current_node = self._root

        if value < current_node.value:
            if current_node.left is not None:
                return self.insert_value(value, current_node.left)
            else:
                current_node.left = insertedNode
        elif value >= current_node.value:
            if current_node.right is not None:
                return self.insert_value(value, current_node.right)
            else:
                current_node.right = insertedNode
        return value

    # TODO: Implement iterative search method

    def search_iteratively(self, value):
        current_node = self.root
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False


    # TODO: Implement recursive search method
    def search_recursively(self, value, current_node=False):
        if current_node is False:
            current_node = self.root
        if current_node is None:
            return False
        if value < current_node.value:
            return self.search_recursively(value, current_node.left)
        elif value > current_node.value:
            return self.search_recursively(value, current_node.right)
        else:
            return True



tree = BST()
print(tree._root)                         # None

# 1. Test node value insertion
# tree.insert_value(3)
tree.insert_value(10)
tree.insert_value(5)
tree.insert_value(16)
tree.insert_value(1)
tree.insert_value(7)
tree.insert_value(16)
print(tree.root.value)                  # 10
print(tree.root.left.value)            # 5
print(tree.root.right.value)           # 16
print(tree.root.left.left.value)      # 1
print(tree.root.left.right.value)     # 7
print(tree.root.right.right.value)    # 16

# # 2. Test iterative search
empty_tree = BST()
print(empty_tree.search_iteratively(10))  # False
print(tree.search_iteratively(10))        # True
print(tree.search_iteratively(7))         # True
print(tree.search_iteratively(-1))        # False

# # 3. Test recursive search
print(empty_tree.search_recursively(10))  # False
print(tree.search_recursively(10))        # True
print(tree.search_recursively(7))         # True
print(tree.search_recursively(-1))        # False
