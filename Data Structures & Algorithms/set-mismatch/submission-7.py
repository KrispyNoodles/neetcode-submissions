class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # duplicate
        dup = sum(nums)-sum(set(nums))

        # missing
        miss = sum(range(1,len(nums)+1))-sum(set(nums))
        
        return [dup, miss]
        