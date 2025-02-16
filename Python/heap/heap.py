class MaxHeap:

    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_idx = self._parent(current_index)

        while True:
            if self.heap[parent_idx] < self.heap[current_index]:
                self._swap(parent_idx, current_index)
                current_index = parent_idx
                parent_idx = self._parent(current_index)
            if self.heap[0] >= value:
                break

    def insert_min(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_idx = self._parent(current_index)

        while True:
            if self.heap[parent_idx] > self.heap[current_index]:
                self._swap(parent_idx, current_index)
                current_index = parent_idx
                parent_idx = self._parent(current_index)
            if self.heap[0] <= value:
                break
    def _sink_down(self, index):
        max_index = 0
        while True:
            left_parent_index = self._left_child(index)
            right_parent_index = self._right_child(index)

            if self.heap[left_parent_index] and self.heap[left_parent_index] > self.heap[index]:
                max_index = left_parent_index

            if self.heap[right_parent_index] and self.heap[right_parent_index] > self.heap[index]:
                max_index = right_parent_index

            if max_index != index:
                self._swap(index, max_index)
                max_index = index
            else:
                return
    def _sink_down_min(self, index):
        max_index = 0
        while True:
            left_parent_index = self._left_child(index)
            right_parent_index = self._right_child(index)

            if self.heap[left_parent_index] and self.heap[left_parent_index] < self.heap[index]:
                max_index = left_parent_index

            if self.heap[right_parent_index] and self.heap[right_parent_index] < self.heap[index]:
                max_index = right_parent_index

            if max_index != index:
                self._swap(index, max_index)
                max_index = index
            else:
                return
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0] = self.heap.pop()
        self._sink_down(0)

    def remove_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0] = self.heap.pop()
        self._sink_down_min(0)

myheap = MaxHeap()
myheap.insert_min(95)
myheap.insert_min(75)
myheap.insert_min(80)
myheap.insert_min(55)
myheap.insert_min(60)
myheap.insert_min(50)
myheap.insert_min(65)
myheap.insert_min(1)

print(myheap.heap)

myheap.remove_min()
#
print(myheap.heap)
#
myheap.remove_min()

print(myheap.heap)
"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""

# myheap = MaxHeap()
# myheap.insert(99)
#
# myheap.insert(72)
# myheap.insert(61)
#
# myheap.insert(58)
#
# print(myheap.heap)
#
# myheap.insert(100)
#
# print(myheap.heap)
#
# myheap.insert(75)
#
# print(myheap.heap)
