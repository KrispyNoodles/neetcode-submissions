class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        subset = []

        def dfs(i):

            # adding the answer into the subset
            if i>=len(nums):
                answer.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            # incrementing i
            dfs(i+1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return answer
