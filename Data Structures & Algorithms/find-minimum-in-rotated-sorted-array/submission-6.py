class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while right>left:
            m = (right+left-1)//2

            if nums[right]>nums[m]:
                right = m
            else:
                left = m+1

        return nums[left]
