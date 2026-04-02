class MinStack:

    def __init__(self):
        # creating a stack in self
        self.stack = []

    def push(self, val: int) -> None:

        # appending to the stack
        self.stack.append(val)
        

    def pop(self) -> None:

        # poping
        self.stack.pop()
        

    def top(self) -> int:

        # retrieving the highest val
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
