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

        self.length += 1

    def prepend(self, *, value):

        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node
        self.length += 1

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


l = LinkList(value=3)
l.append(value=7)
l.append(value=10)
l.prepend(value=15)
l.insert(idx=4, value=60)
l.print_ll()