# stack uses last-in-first-out (LIFO) and queue usese (FIFO)
# pop left and enter from the right

# Definition for douvly-linked list.
class ListNode:
    def __init__(self, val=int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None        

    # enters from the right (to the tail)
    def push(self, x: int) -> None:
        
        node_added = ListNode(x)

        # if there is no element before, replace the head and tail
        if self.empty():
            
            self.head = node_added
            self.tail = node_added
            return

        # else it is a new node added to the tail
        self.tail.next = node_added
        node_added.prev = self.tail

        # update the tail
        self.tail = node_added      
        
    # pop from the head
    def pop(self) -> int:

        # if there is no element
        if self.empty():
            return -1

        # retrieve the value for the head
        val_return  = self.tail.val

        # shifting the head
        new_tail = self.tail.prev
        self.tail = new_tail
        

        # checking if there is only a single node left
        if self.tail != None:
            print('condition fulfiled')
            self.tail.next = None
        
        else:
            self.head = None
            self.tail = None
            
        return val_return

    # returns the element at the top of the stack
    # which refers to the one that is last entered
    def top(self) -> int:
        
        # if there is no element
        if self.empty():
            return -1
        else:
            return self.tail.val
        

    def empty(self) -> bool:

        # if there is no element
        if self.head == None:
            return True

        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()