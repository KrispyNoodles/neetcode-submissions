# double ended queue
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # poping one of the queue
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        pop_val = self.q1.pop()
        return pop_val

    def top(self) -> int:

        # retrieve the latest element of the queue
        return self.q1[-1]

    def empty(self) -> bool:

        if self.q1 == deque():
            return True
        else:
            return False
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()