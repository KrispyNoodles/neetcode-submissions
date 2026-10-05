class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        nums_decrease = sorted(nums, reverse=True)
        nums_increase = sorted(nums, reverse=False)

        if nums == nums_decrease or nums==nums_increase:
            return True
        return False