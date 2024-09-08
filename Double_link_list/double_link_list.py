class NewNode:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.prev = None


class DoubleLinkList:
    def __init__(self, value):
        new_node = NewNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = NewNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print_dl(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
        # print('my prev value ', self.tail.prev.value)

    def pop(self):
        if self.length == 0:
            return None
        temp_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp_node.prev = None
            self.length -= 1
        return temp_node

    def prePend(self, value):
        new_node = NewNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):
        temp_node = self.head.next
        self.head = temp_node
        temp_node.prev = None



c = DoubleLinkList(7)
c.append(5)
c.append(8)
c.pop()
c.prePend(10)
# c.print_dl()
# c.popFirst()
c.print_dl()
