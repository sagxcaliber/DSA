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
        if 0 > idx > self.length:
            return False
        if self.length > 0 and idx == 1:
            self.prepend(value=value)

        if idx == self.length + 1:
            self.append(value=value)

        new_node = Node(value=value)
        temp_node = self.get(index=idx - 1)
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length = self.length + 1
        return True
        # elif idx <= self.length:
        #     temp_node = self.head
        #     new_node = Node(value=value)
        #     for x in range(1, idx - 1):
        #         temp_node = temp_node.next
        #
        #     new_node.next = temp_node.next
        #     temp_node.next = new_node
        #     self.length += 1

    def remove(self, index):
        if index == 1:
            self.pop_from_first()
            return True
        if 0 > index > self.length:
            print("inside Error code 0 index")
            return False
        if index == self.length - 1:
            self.pop()
        temp_node = self.get(index=index - 1)
        deleting_node = temp_node.next
        if deleting_node.next is not None:
            temp_node.next = deleting_node.next
            deleting_node.next = None
        else:
            temp_node.next = None
        return True

    def pop_from_first(self):
        temp_node = self.head.next
        self.head = temp_node
        self.length -= 1

    def get(self, index):
        if self.length > 0 and index <= self.length :
            temp_node = self.head
            for _ in range(1, index):
                temp_node = temp_node.next
            return temp_node

    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        else:
            return False

    def pop(self, index=None):
        temp_node = self.head
        pre_node = self.head
        if index:
            for x in range(1, index):
                pre_node = temp_node
                temp_node = temp_node.next
            pre_node.next = temp_node.next

        elif index and (index == 0 or index > self.length):
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

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp_node.value

    def reverse(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = self.head
        before = None
        for _ in range(self.length):
            after = temp_node.next
            temp_node.next = before
            before = temp_node
            temp_node = after


l = LinkList(value=1)
# l.pop_from_first()
l.append(value=2)
l.append(value=3)
l.append(value=4)
l.reverse()
l.print_ll()
# l.set(4, 150)
# l.print_ll()
# print('###################')
# l.prepend(value=15)
# l.prepend(value=20)
# l.prepend(value=40)
# l.prepend(value=60)
# print(l.length,'@')
# print(l.get(2),'get value by index')
# l.pop()
# l.insert(idx=4, value=60)
# print(l.length,'length')
# l.set(4, 100)
# l.remove(2)
# l.print_ll()
