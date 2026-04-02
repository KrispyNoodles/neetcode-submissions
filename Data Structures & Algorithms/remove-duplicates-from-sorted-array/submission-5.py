# two pointers (soln)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0

        # whhile right is less than the length
        while right < n:
            
            # initialise for both to be the same
            # this too reassigns future values
            nums[left] = nums[right]

            # while right is more than left and if the values are the same
            # move the right pointer
            while right < n and nums[right] == nums[left]:
                right += 1
            
            # after reaching the last value of the same segment, move the left by 1
            left += 1

        # the (left-1) index will be the last updated value
        # but the length will be based on the left value
        return left