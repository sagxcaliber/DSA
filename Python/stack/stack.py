class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = NewNode(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def push(self, value):
        new_node = NewNode(value)
        if self.height == 0:
            self.top = new_node
            self.bottom = new_node
            self.height += 1
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        self.height -= 1
        print('pop from stack : ', temp_node.value)
        return temp_node

    def printStack(self):
        temp_node = self.top
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


s = Stack(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.pop()
s.pop()
s.printStack()
