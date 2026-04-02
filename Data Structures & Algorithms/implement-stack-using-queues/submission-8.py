# using two queue
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.temp_queue = deque()

    # queues are only able to pop from the left
    # but we want to do it from the right because of the property of LIFO of a stack
    def push(self, x: int) -> None:

        self.temp_queue.append(x)

        # moving all the values from the oriignal queue to the temp quueue
        # and queues can only pop left
        # to remain the order of LIFO

        # when adding in 4
        # instead of (1,2,3,4)

        # it becomes, so that popleft can be done to ensure the LIFO
        # (4,1,2,3)
        while self.queue:
            pop_val = self.queue.popleft()
            self.temp_queue.append(pop_val)

        # reassign
        self.queue, self.temp_queue = self.temp_queue, self.queue 


    def pop(self) -> int:
        pop_val = self.queue.popleft()
        return pop_val

    def top(self) -> int:

        # retrieve the latest element of the queue
        return self.queue[0]

    def empty(self) -> bool:

        if self.queue == deque():
            return True
        else:
            return False

# time compleixty of O(1)
# space complexity of O(n)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()