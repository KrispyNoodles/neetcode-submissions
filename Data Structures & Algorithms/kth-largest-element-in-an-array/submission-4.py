import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        new_heap = []
        heapq.heapify(new_heap)

        # for all values convert into a negative
        for i in nums:
            heapq.heappush(new_heap, -i)

        while k>0:

            pop_val = heapq.heappop(new_heap)
            k-=1

        return -pop_val