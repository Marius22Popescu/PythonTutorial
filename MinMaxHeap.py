class Heap(object):
    def __init__(self):
        self.__array = []
        self.__last_index = -1

    def push(self, value):
        """
            Append item on the back of the heap,
            sift upwards if heap property is violated.
        """
        self.__array.append(value)
        self.__last_index += 1
        self.__siftup(self.__last_index)

    def pop(self):
        """
            Pop root element from the heap (if possible),
            put last element as new root and sift downwards till
            heap property is satisfied.

        """
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        if self.__last_index > 0:  # more than one element in the heap
            self.__array[0] = self.__array[self.__last_index]
            self.__siftdown(0)
        self.__last_index -= 1
        return root_value

    def peek(self):
        """ peek at the root, without removing it """
        if not self.__array:
            return None
        return self.__array[0]

    def replace(self, new_value):
        """ remove root & put NEW element as root & sift down -> no need to sift up """
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        self.__array[0] = new_value
        self.__siftdown(0)
        return root_value

    def heapify(self, input_list):
        """
            each leaf is a trivial subheap, so we may begin to call
            Heapify on each parent of a leaf.  Parents of leaves begin
            at index n/2.  As we go up the tree making subheaps out
            of unordered array elements, we build larger and larger
            heaps, joining them at the i'th element with Heapify,
            until the input list is one big heap.
        """
        n = len(input_list)
        self.__array = input_list
        self.__last_index = n-1
        for index in reversed(range(n//2)):
            self.__siftdown(index)

    @classmethod
    def createHeap(cls, input_list):
        """
            create an heap based on an inputted list.
        """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def __siftdown(self, index):
        current_value = self.__array[index]
        left_child_index, left_child_value = self.__get_left_child(index)
        right_child_index, right_child_value = self.__get_right_child(index)
        # the following works because if the right_child_index is not None, then the left_child
        # is also not None => property of a complete binary tree, else left will be returned.
        best_child_index, best_child_value = (right_child_index, right_child_value) if right_child_index\
        is not None and self.comparer(right_child_value, left_child_value) else (left_child_index, left_child_value)
        if best_child_index is not None and self.comparer(best_child_value, current_value):
            self.__array[index], self.__array[best_child_index] =\
                best_child_value, current_value
            self.__siftdown(best_child_index)
        return


    def __siftup(self, index):
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent(index)
        if index > 0 and self.comparer(current_value, parent_value):
            self.__array[parent_index], self.__array[index] =\
                current_value, parent_value
            self.__siftup(parent_index)
        return

    def comparer(self, value1, value2):
        raise NotImplementedError("Should not use the baseclass heap\
            instead use the class MinHeap or MaxHeap.")

    def __get_parent(self, index):
        if index == 0:
            return None, None
        parent_index =  (index - 1) // 2
        return parent_index, self.__array[parent_index]

    def __get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__array[right_child_index]

    def __repr__(self):
        return str(self.__array[:self.__last_index+1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.__array == other.__array
        if isinstance(other, list):
            return self.__array == other
        return NotImplemented

class MinHeap(Heap):
    def comparer(self, value1, value2):
        return value1 < value2

class MaxHeap(Heap):
    def comparer(self, value1, value2):
        return value1 > value2


def manualTest():
    """
        Basic test to see step by step changes.
    """
    h = MinHeap()
    h.push(10)
    assert(h == [10])
    h.push(20)
    assert(h == [10, 20])
    h.push(5)
    assert(h == [5, 20, 10])
    h.push(8)
    assert(h == [5, 8, 10, 20])
    h.push(3)
    assert(h == [3, 5, 10, 20, 8])
    h.push(40)
    assert(h == [3, 5, 10, 20, 8, 40])
    h.push(50)
    assert(h == [3, 5, 10, 20, 8, 40, 50])
    h.push(1)
    assert(h == [1, 3, 10, 5, 8, 40, 50, 20])
    assert(h.pop() == 1)
    assert(h.pop() == 3)
    assert(h.pop() == 5)
    assert(h.pop() == 8)
    assert(h.pop() == 10)
    assert(h.pop() == 20)
    assert(h.pop() == 40)
    assert(h.pop() == 50)
    try:
        h.pop()
        assert(False)
    except IndexError:  # check if assertion is thrown when heap is empty
        assert(True)
    # check createHeap classmethod.
    assert(MinHeap.createHeap([2,7,3,1,9,44,23]) == [1, 2, 3, 7, 9, 44, 23])
    assert(MaxHeap.createHeap([2,7,3,1,9,44,23]) == [44, 9, 23, 1, 7, 3, 2])


def automaticTest(sample_size):
    """
        Test creating a min & max heap, push random values
        on it and see if the popped values are sorted.
    """
    import random
    random_numbers = random.sample(range(100), sample_size)
    min_heap = MinHeap()
    max_heap = MaxHeap()
    for i in random_numbers:
        min_heap.push(i)
        max_heap.push(i)
    random_numbers.sort()
    for i in random_numbers:
        assert(min_heap.pop() == i)
    random_numbers.sort(reverse=True)
    for i in random_numbers:
        assert(max_heap.pop() == i)

automaticTest(20)
manualTest()