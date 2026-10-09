class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, total):

            if i==len(nums):
                return total

            # increment i and add it into the total
            # one takes the value and the other skips the value to be addded to add the next combi
            value = dfs(i+1, total^nums[i]) + dfs(i+1, total)
            return value
        
        return dfs(0, 0)


