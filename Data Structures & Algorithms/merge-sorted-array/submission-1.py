from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # remove all 0's in nums1
        coutner = 0

        for index, value in enumerate(nums1):
           
            if index > m-1:
                nums1[index] = nums2[coutner]
                coutner+=1

        nums1.sort()
        print(nums1)

# complexity of O(n) because of looping through nums1
