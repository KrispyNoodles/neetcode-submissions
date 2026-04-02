class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1

        while right >= left:

            middle = (right+left)//2

            # this means the value is on the left
            if nums[middle] > target:
                right = middle-1

            elif nums[middle] < target:
                left = middle+1
            else:
                return middle

        return -1
