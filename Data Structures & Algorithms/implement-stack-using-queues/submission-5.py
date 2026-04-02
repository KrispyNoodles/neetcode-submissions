from collections import deque

# model asnwer
# queue of queues
# stack uses last-in-first-out (LIFO)
class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:

        # creating a new queue that adds in from the right
        # x = 1
        # self.q will be the previous queue in there
        # however this creates an inconsistent data struct of sometimes, dequeue and sometimes a value...
        # deque([deque(['2'], '1')])

        self.q = deque([self.q, x])
        print(self.q)
    
    def pop(self) -> int:

        # poping from the right
        top = self.q.pop()

        print(self.q)

        self.q = self.q.pop()
        print(self.q)

        return top
        
    def top(self) -> int:

        return self.q[1]
        

    def empty(self) -> bool:

        if self.q == None:
            return True
        else:
            return False
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()