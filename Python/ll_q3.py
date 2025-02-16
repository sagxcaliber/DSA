class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(my_linked_list, value):
    """

    1,2,3,4,5
    1,2,3,4,5
    1,2,
    1,3,5
    """
    if value == 1:
        return my_linked_list.tail
    else:
        slow = my_linked_list.head
        fast = my_linked_list.head
        while fast is not None:
            for _ in range(value):
                if fast is not None:
                    fast = fast.next
                else:
                    fast = None
            slow = slow.next
        return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 5
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
