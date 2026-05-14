from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        answer = 0 

        for number in nums:

            answer = answer^number
        
        return answer