class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, total):

            if i==len(nums):
                return total

            # increment i and add it into the total
            value = dfs(i+1, total^nums[i]) + dfs(i+1, total)
            return value
        
        return dfs(0, 0)


