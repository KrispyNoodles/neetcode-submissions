class MinStack:

    # initialise stack
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        
        # append a value into the stack
        self.stack.append(val)        

    def pop(self) -> None:

        # poping a value
        self.stack.pop()
    
    def top(self) -> int:

        # retreiving teh top value
        return self.stack[-1]
        
    def getMin(self) -> int:

        # retrieivng the min value
        return min(self.stack)
        