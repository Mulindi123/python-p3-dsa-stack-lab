class Stack:

    def __init__(self, items = None, limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
            return True
        else:
            return False #"Stack is full, cannot push more items!"

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None
        

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1] # Return the last (top) element on the list
        else:
            return None  # Stack is empty, there is nothing to peek
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) ==self.limit:
            return True
        else:
            return False

    def search(self, target):
        if target in self.items:
            return target
        return -1
