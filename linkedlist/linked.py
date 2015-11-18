__author__ = 'Henry Pan'


class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    """
    1. insert
    2. size
    3. search
    4. delete
    """
    def __init__(self, head=None):
        self.head = head

    # insert at the head of the linkedlist
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count = 1
        t_head = self.head
        while t_head.get_next():
            count += 1
            t_head = t_head.get_next()
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = self.head.get_next()
        if current is None:
            raise ValueError("Data not found")
        return None

    def delete_node(self, data):
        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                break
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('No data found')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def get_head(self):
        return self.head


def one_by_one():
    tail = Node(10)
    node1 = Node(1, tail)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    head = Node(10, node3)
    while head.get_next():
        print 'Current data: ', head.data
        head = head.get_next()
    print 'Current data: ', head.data


if __name__ == '__main__':
    node1 = Node(10)
    llist = LinkedList(node1)
    print llist.get_head().get_data()

    llist.insert(30)
    print llist.get_head().get_data()

    llist.insert(20)
    print llist.get_head().get_data()

    head = llist.get_head()
    while head.get_next():
        print 'Current data: ', head.data
        head = head.get_next()
    print 'Current data: ', head.data
    print 'Current size: ', llist.size()
    found_node = llist.search(30)
    print found_node.get_data()
    found_node.set_next(None)

    # llist.delete_node(30)
    head = llist.get_head()
    while head.get_next():
        print 'Current data: ', head.data
        head = head.get_next()
    print 'Current data: ', head.data
