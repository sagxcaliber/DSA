
class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = NewNode(value)
        self.top = new_node
        self.bottom = new_node

    def push(self, value):
        new_node = NewNode(value)
        temp_node = self.top
        self.top = new_node
        self.top.next = temp_node

    def pop(self):
        temp_node = self.top.next
        self.top = temp_node

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
s.printStack()

