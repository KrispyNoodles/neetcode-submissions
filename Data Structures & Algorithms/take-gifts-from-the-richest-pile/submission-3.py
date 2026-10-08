from heapq import heapify 
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        # heap is always min by defualt

        # throw it into a hip
        for i in range(len(gifts)):
            gifts[i]=-gifts[i]
        
        heapq.heapify(gifts)

        # pop the value then append it back in
        for _ in range(k):
            
            # have to make it positive because cannot sqrt negative
            add_back = heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.sqrt(-add_back)))

        return -sum(gifts)