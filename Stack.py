class Stack:
    def __init__(self):
        self.listElements = []

    def push(self, element):
        self.listElements.append(element)

    def pop(self):
        return self.listElements.pop()

    def peek(self):
        return self.listElements[len(self.listElements)-1]

    def size(self):
        return len(self.listElements)

    def isEmpty(self):
        return self.listElements == []


st = Stack()

print(st.isEmpty())
print("The size of stack is: ", st.size())
for i in range (1, 10):
    st.push(i)
for j in range (1, 4):
    print("pop: ", st.pop())
print("The size of stack is: ", st.size())
print(st.isEmpty())
print("The peek element is: ", st.peek())
