class MyQueue(object):
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[0]

    def pop(self):
        return self.stack.pop(0)

    def put(self, value):
        self.stack.append(value)
