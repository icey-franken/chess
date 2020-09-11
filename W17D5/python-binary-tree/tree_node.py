# TODO: Implement TreeNode class

class TreeNode():
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


# node_a = TreeNode('a')
# print(node_a.value)         # 'a'
# print(node_a.right)         # None
# print(node_a.left)          # None

# node_b = TreeNode('b')
# node_a.left = node_b
# print(node_a.left.value)    # 'b'
# print(node_a.right)         # None
