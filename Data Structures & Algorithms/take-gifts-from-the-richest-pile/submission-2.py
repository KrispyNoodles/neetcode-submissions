import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        # sort first
        for _ in range(k):

            # max index
            max_idx = 0

            # find the largest pile
            for i in range(1, len(gifts)):
                # find the biggest edit and leav eloop
                if gifts[i] >= gifts[max_idx]:
                    max_idx = i

            # convert to int
            gifts[max_idx] = int(math.sqrt(gifts[max_idx]))

        return sum(gifts)