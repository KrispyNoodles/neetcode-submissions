import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums

        # convert it into a heap
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:

        # when a value is added, pop and then add
        
        # add the val in
        heapq.heappush(self.nums, val)

        # ensure that there are only k vals inside
        while len(self.nums) >self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]


        
