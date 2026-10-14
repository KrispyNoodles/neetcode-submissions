class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # doing recursion to add all
        def dfs(i, total):

            # I can either skip this value or add it
            if i==len(nums):
                return total
            
            answer = dfs(i+1, total^nums[i]) + dfs(i+1, total)

            return answer

        return dfs(0,0)