class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, sum_val):

            # when reach the end
            if i>=len(nums):
                return sum_val

            # can choose to either add this number of skip
            return dfs(i+1,  sum_val^nums[i]) + dfs(i+1,  sum_val) 
        
        return dfs(0, 0)