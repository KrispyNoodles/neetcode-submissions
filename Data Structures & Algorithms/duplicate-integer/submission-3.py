class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        countMap = {}

        for i in nums:

            # if inside add it in
            if i not in countMap:
                countMap[i] = 1
            else:
                print('found dupe')
                return True
        
        # if condition passes then it is all unique
        return False