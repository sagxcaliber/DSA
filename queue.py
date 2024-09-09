class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = NewNode(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def Enqueue(self, value):
        new_node = NewNode(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1
        return True

    def Dequeue(self):

        if self.length == 0:
            return None
        temp_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp_node.next = None
            print('Dequeue : ', temp_node.value)
        self.length -= 1
        return temp_node

    def print_queue(self):
        temp_node = self.first
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


qu = Queue(1)
qu.print_queue()

qu.Enqueue(2)
qu.Enqueue(3)
qu.Dequeue()

qu.print_queue()
