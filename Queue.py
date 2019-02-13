class Queue():
    def __init__(self):
        self.listElements = []

    def enqueue(self, element):
        self.listElements.append(element)

    def dequeue(self):
        return self.listElements.pop(0)

    def peek(self):
        return self.listElements[0]

    def isEmpty(self):
        return self.listElements == []

    def size(self):
        return len(self.listElements)


que = Queue()

print(que.isEmpty())
print("The size of stack is: ", que.size())
for i in range (1, 10):
    que.enqueue(i)
for j in range (1, 4):
    print("dequeue: ", que.dequeue())
print("The size of stack is: ", que.size())
print(que.isEmpty())
print("The peek element is: ", que.peek())