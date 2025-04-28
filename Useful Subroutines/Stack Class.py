class Stack():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
    
    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
        else:
            raise Exception("Stack full.")
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack empty.")
            return None
    
    def isFull(self):
        return len(self.stack) == self.maxSize
    
    def isEmpty(self):
        return len(self.stack) == 0

    
