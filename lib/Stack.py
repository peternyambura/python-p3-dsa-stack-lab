class Stack:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full!")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty!")

    def size(self):
        return len(self.items)

    def empty(self):
        return self.is_empty()

    def full(self):
        return self.limit is not None and len(self.items) == self.limit

    def search(self, value):
        try:
            distance = len(self.items) - 1 - self.items[::-1].index(value)
            return distance
        except ValueError:
            return -1
