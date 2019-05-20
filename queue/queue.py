class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __repr__(self):
        return '{}'.format(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        value = self.head.get_value()
        if not self.head.get_next():
            self.head = None
            self.tail = None
            return value

        self.head = self.head.get_next()

        return value

    def contains(self, value):

        if not self.head:
            return False

        if self.head.get_value() == value or self.tail.get_value() == value:
            return True
        
        current = self.head
        
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    self.storage.remove_head()

  def len(self):
    len(self.storage)
