class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # using binary search

        left,right = 0, len(nums)-1

        # the switch is where the answer is
        while right>left:

            middle = (right+left)//2

            # this means the value is from the middle+1 to the right
            if nums[middle]>=nums[right]:
                left = middle+1
            else:
                # this means the value is from the left to the middle
                right = middle

        return nums[left]
