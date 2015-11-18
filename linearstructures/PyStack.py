__author__ = 'Henry Pan'


class Stack:
    """
    FILO: First In Last Out
    1. stack()
    2. push()
    3. pop()
    4. peak()
    5. is_empty()
    6. size()
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item_out = self.items[-1]
        del self.items[-1]
        return item_out

    # list has the method pop() already
    def pop_2(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


### Assignment, write a function revstring that uses a stack to reverse the characters in a string
def revstring(mystr):
    my_stack = Stack()
    my_list = []
    for a in mystr:
      my_stack.push(a)
    while not my_stack.is_empty():
      my_list.append(my_stack.pop())
    return ''.join(my_list)


if __name__ == '__main__':
    my_stack = Stack()

    my_stack.push('one')
    my_stack.push('two')
    my_stack.push('three')

    for i in range(3):
        print my_stack.peek()

    print 'After peek, size of my stack:', my_stack.size()

    while not my_stack.is_empty():
        print my_stack.pop()

    print 'After pop, size of my stack:', my_stack.size()

    # Test #revstring()
    assert(revstring('apple') == 'elppa')
    assert(revstring('x') == 'x')
    assert(revstring('1234567890') == '0987654321')

