# Definition for douvly-linked list.
class ListNode:
    def __init__(self, val=int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):

        # creating a head and a tail of the queue
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        
        if self.head == None:
            return True
        else:
            return False

    def append(self, value: int) -> None:

        node_added = ListNode(value)

        # if it is empty
        if self.isEmpty():
            self.head = node_added
            self.tail = node_added
            return
        
        # else...
        self.tail.next = node_added

        # add the previous for the node_added back to the old tail
        # typo of using tail instead of prev
        node_added.prev = self.tail

        self.tail = node_added

    def appendleft(self, value: int) -> None:
        
        node_added = ListNode(value)

        # checking if it is empty
        # if it is empty
        if self.isEmpty():
            self.head = node_added
            self.tail = node_added
            return

        # add the next for the node_added
        node_added.next = self.head

        # add the prev for the prev self.head
        self.head.prev = node_added

        self.head = node_added

    def pop(self) -> int:

        if self.isEmpty():
            return -1

        print(self.tail)
        # pop val removed
        pop_val = self.tail.val

        # if there is only one element left
        if self.tail.prev is None:
            self.tail = None
            self.head = None
            return pop_val

        # moving the tail node
        self.tail = self.tail.prev
        
        self.tail.next = None

        return pop_val
        

    def popleft(self) -> int:

        if self.isEmpty():
            return -1

        # pop_val
        pop_left_val = self.head.val

        # if there is only one element left, reset
        if self.head.next is None:
            self.tail = None
            self.head = None
            return pop_left_val
        
        # moving the head node
        self.head = self.head.next
        self.head.prev = None

        return pop_left_val

# time complexity of O(1)
# space complexity of O(1)