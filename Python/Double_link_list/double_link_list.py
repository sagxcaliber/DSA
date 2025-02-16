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
        return temp_node.value

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
        if self.length == 0:
            return None
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp_node.next = None
        self.length -= 1
        return temp_node.value

    def get(self, index):
        if 0 < index >= self.length:
            return None
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            # print(temp_node.value)
            return temp_node

    def set_value(self, index, value):
        node = self.get(index)
        node.value = value
        return True

    def insert(self, index, value):

        if index == 0:
            return self.prePend(value)
        elif 0 < index > self.length:
            return False
        elif index == self.length:
            return self.append(value)
        else:
            new_node = NewNode(value)
            current_node = self.get(index)
            temp_node = current_node.prev
            temp_node.next = new_node
            new_node.next = current_node
            new_node.prev = temp_node
            current_node.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if 0 < index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        current_node = self.get(index)
        current_node.next.prev = current_node.prev
        current_node.prev.next = current_node.next
        current_node.prev = None
        current_node.next = None
        self.length -= 1
        return current_node.value




c = DoubleLinkList(7)
c.append(5)
c.append(8)
# c.get(2)
# c.set_value(2,3)
# c.insert(2, 1)
# c.insert(2, 10)
# c.pop()
# c.prePend(10)
# c.print_dl()
# c.popFirst()
print(c.remove(2),'\n')

c.print_dl()
