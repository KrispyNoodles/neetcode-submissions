import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        new_list = []

        # convert to negative
        for i in nums:
            new_list.append(-i)
        
        # creating a heap
        heapq.heapify(new_list)

        # poping till there are k elements inside, then return the "smallest"
        for i in range(k):
            answer = heapq.heappop(new_list)

        # putting negative back
        return -answer
