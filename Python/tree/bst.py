class NewNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = NewNode(value)
        temp = self.root

        if self.root is None:
            self.root = new_node
            return True

        while temp:
            if value == temp.value:
                return False
            if temp.value > value and temp.left is None:
                temp.left = new_node
                return True
            if temp.value < value and temp.right is None:
                temp.right = new_node
                return True
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
        else:
            return False


b = BinarySearchTree()
b.insert(5)
b.insert(4)
b.insert(3)
b.insert(7)
b.insert(1)
b.insert(2)
b.insert(6)
print(b.contains(7))
# print(b.root.value)
# print(b.root.left.value)
# print(b.root.right.value)
# print(b.root.left.left.value)
# print(b.root.left.left.right.value)
