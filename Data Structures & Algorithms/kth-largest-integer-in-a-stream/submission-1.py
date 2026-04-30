import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # biggest
        self.k = k

        # creating a heap
        self.nums = nums

        # convert it into a heap
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int: 
        
        # add the new val in
        heapq.heappush(self.nums, val)

        # poping till there is left with the len of k
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)

        print(self.nums)
    
        return self.nums[0]

        



        
