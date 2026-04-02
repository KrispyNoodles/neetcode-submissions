from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):

        # create head and tail nodes
        # head ---> ..... ---> tail

        self.head = None
        self.tail = None     
    
    def get(self, index: int) -> int:

        i = 0
        curr = self.head

        while curr != None and i<=index:

            print(curr.val)

            # find the previous pointer
            if i == index:
                return curr.val

            i += 1
            curr = curr.next

        # it iterated through and cant find
        return -1

    def insertHead(self, val: int) -> None:

        # create a new node, since it is the new head it points at nothing
        node_created = ListNode(val, None)

        # update the previous head to point to this
        # if it exists
        if self.head is None:
            self.head = node_created
            self.tail = node_created
            return 
        
        # update the head
        # node_created --> head --....
        node_created.next = self.head
        self.head = node_created
        

    def insertTail(self, val: int) -> None:

        # create a new node, since it is the new head it points at nothing
        node_created = ListNode(val, None)

        # if the list is empty
        if self.head is None:
            self.head = node_created
            self.tail = node_created
            return 
        
        # else
        # tail --> node_created --> none
        self.tail.next = node_created
        
        # update the tail
        self.tail = node_created
        
    def remove(self, index: int) -> bool:
        
        # move from tail up
        curr = self.head
        i = 0
        prev_pointer = None

        # updating the head, if the head is being removed
        # checking if the head exists
        if index==0:
            if self.head != None:
                self.head = self.head.next
                return True
            else:
                return False

        while curr != None and i<=index:

            # find the previous pointer
            if i == index-1:
                prev_pointer = curr
                
            # when reaching the current to be removed
            # update the previous pointer to point to the current next
            if i == index:
                # updating the tail together
                if self.tail == curr:
                    self.tail = prev_pointer
                    prev_pointer.next=None
                
                else:
                    prev_pointer.next = curr.next
                return True     
    
            # increment i and move curr
            i += 1
            curr = curr.next

        # index is out
        return False


    def getValues(self) -> List[int]:

        curr = self.head
        list_to_return = []

        # loop through all the values in the list
        while curr != None:
            list_to_return.append(curr.val)
            curr = curr.next

        return list_to_return

