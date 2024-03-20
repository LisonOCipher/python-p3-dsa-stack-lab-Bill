class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def __str__(self):
        return f"Stack: {self.items}"

    def clear(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1
