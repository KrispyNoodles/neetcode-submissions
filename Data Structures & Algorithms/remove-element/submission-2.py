# trying again
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        temp_arr = []

        for value in nums:
            if value != val:
                temp_arr.append(value)

        # reassining the valyues
        nums[:len(temp_arr)] = temp_arr

        return len(temp_arr)