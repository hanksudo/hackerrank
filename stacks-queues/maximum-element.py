class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            self.max_stack.append(max(value, self.max_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()

    def top(self):
        return self.stack[-1]

    @property
    def max_value(self):
        return self.max_stack[-1]

stack = Stack()
for _ in range(int(input())):
    cmd = input()
    if len(cmd) > 1:
        query, num = cmd.split(" ")
    else:
        query = cmd

    if query == "1":
        stack.push(int(num))
    elif query == "2":
        stack.pop()
    elif query == "3":
        print(stack.max_value)
