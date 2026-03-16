class Node:
    def __init__(self, value, next:None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value, self.top)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def printStack(self):
        while self.top is not None:
            print(f"{self.top.value} -> ", end="")
            self.top = self.top.next


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.printStack()
