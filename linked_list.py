class Node:
    def __init__(self, *, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, *, value):
        self.node = Node(value=value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    def print_ll(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, *, value):
        new_node = Node(value=value)
        self.tail.next = new_node
        self.tail = new_node
        self.length = self.length + 1

    def prepend(self, *, value):

        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node
        self.length = self.length + 1

    def insert(self, *, idx, value):

        if self.length > 0 and idx == 1:
            self.prepend(value=value)

        elif idx == self.length + 1:
            self.append(value=value)

        elif idx <= self.length:
            temp_node = self.head
            new_node = Node(value=value)
            for x in range(1, idx - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def pop_from_first(self):
        temp_node = self.head.next
        self.head = temp_node
        self.length -= 1

    def get(self, index):
        if self.length > 0:
            temp_node = self.head
            for _ in range(1, index):
                temp_node = temp_node.next
            return temp_node.value

    def set(self, index, value):
        if 0 < self.length >= index != 0:
            temp_nope = self.head
            for _ in range(1, index):
                temp_nope = temp_nope.next
            temp_nope.value = value
            return True
        else:
            raise Exception("Incorrect Index")

    def pop(self, index=None):
        temp_node = self.head
        pre_node = self.head
        if index:
            for x in range(1, index):
                pre_node = temp_node
                temp_node = temp_node.next
            pre_node.next = temp_node.next
        elif index == 0 or index > self.length :
            return
        elif temp_node is not None:
            for _ in range(1, self.length + 1):
                if temp_node.next is not None:
                    pre_node = temp_node
                    temp_node = temp_node.next
                else:
                    self.tail = pre_node
            pre_node.next = None

        print(temp_node.value, '@@@@@@@@@@@@ poped')
        self.length = self.length - 1
        return temp_node.value


l = LinkList(value=3)
# l.pop_from_first()
l.append(value=7)
l.append(value=10)
l.set(4, 150)
# l.print_ll()
print('###################')
# l.prepend(value=15)
# l.prepend(value=20)
# l.prepend(value=40)
# l.prepend(value=60)
# print(l.length,'@')
# print(l.get(2),'get value by index')
# l.pop(0)
# l.insert(idx=4, value=60)
# print(l.length,'length')
l.print_ll()
