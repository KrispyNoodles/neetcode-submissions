class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # similar concept?
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1