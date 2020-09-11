"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here


class Node:
    # TODO: Set the `_value` `_next` node instance variables
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def set_next(self, nextNode):
        self._next = nextNode

    @property
    def value(self):
        return self._value


# TODO: Implement a Singly Linked List class here
class LinkedList:
    # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
    def __init__(self, node=None):
        self._head = node
        self._tail = node
        self._length = len(self)

    @property
    def head(self):
        return self._head

    @head.setter
    def set_head(self, newHead):
        self._head = newHead

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def set_tail(self, newTail):
        self._tail = newTail

    @property
    def length(self):
        return len(self)

    # TODO: Implement the get_node method here
    def get_node(self, position):
        if position < 0 or position > self.length:
            return None
        elif position == 0:
            return self.head
        elif position == self.length - 1:
            return self.tail
        else:
            node = self.head
            i = 0
            while i in range(position):
                node = node.next
                i += 1
            return node

    # TODO: Implement the add_to_tail method here
    def add_to_tail(self, value):
        tailNode = Node(value)
        if self.tail is None:
            self.set_head = tailNode
            pass
        else:
            self.tail.next = tailNode
        self.set_tail = tailNode
        # increase length by one!

    # TODO: Implement the add_to_head method here
    def add_to_head(self, value):
        headNode = Node(value)
        if self.head is None:
            self.set_tail = headNode
        else:
            headNode.set_next = self.head
        self.set_head = headNode
        # increase length by one!

    # TODO: Implement the remove_head method here
    def remove_head(self):
        if self.head is None:
            return 'NO HEAD'
        else:
            self.set_head = self.head.next
            # decrease length by one!

    # TODO: Implement the remove_tail method here
    def remove_tail(self):
        if self.tail is None:
            return 'NO TAIL'
        elif self.length == 1:
            self.set_tail = None
            self.head.set_next = None
            self.set_head = None
        else:
            newTail = self.get_node(self.length - 1)
            newTail.set_next = None
            self.set_tail = newTail

    # TODO: Implement the __len__ method here
    def __len__(self):
        if self.head is None:
            return 0
        else:
            count = 1
            node = self.head
            while node.next is not None:
                count += 1
                node = node.next
            return count

# Phase 2

    # TODO: Implement the contains_value method here
    def contains_value(self, target):
        pass

    # TODO: Implement the insert_value method here
    def insert_value(self, position, value):
        pass

    # TODO: Implement the update_value method here
    def update_value(self, position, value):
        pass

    # TODO: Implement the remove_node method here
    def remove_node(self, position):
        pass

    # TODO: Implement the __str__ method here
    def __str__(self):
        return('''Linked list with head: {0}, tail: {1}, length: {2}'''
               .format(self.head,
                       self.tail,
                       self.length))

# Phase 1 Manual Testing:


# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
# <__main__.LinkedList object at ...>
print(linked_list)

# # 2. Test getting a node by its position
print(linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new tail node`

# # 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
# linked_list.remove_head()
# print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
# print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
# linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
print(len(linked_list))                                 # 2
print(linked_list)

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
# linked_list = LinkedList()
# linked_list.add_to_head('new head node')
# print(linked_list.contains_value('new head node'))      # True
# print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
# linked_list.insert_value(0, 'hello!')
# print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
# linked_list.update_value(0, 'goodbye!')
# print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
# print(linked_list.get_node(1)._value)                   # `new head node`
# linked_list.remove_node(1)
# print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
# new_linked_list = LinkedList()
# print(new_linked_list)                  # Empty List
# new_linked_list.add_to_tail('puppies')
# print(new_linked_list)                  # puppies
# new_linked_list.add_to_tail('kittens')
# print(new_linked_list)                  # puppies, kittens
