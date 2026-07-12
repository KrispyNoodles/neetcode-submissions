class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        current_subset = []

        def helperFunction(i):
            if i>=len(nums):
                answer.append(current_subset.copy())
                return
            
            current_subset.append(nums[i])
            helperFunction(i+1)

            current_subset.pop()
            helperFunction(i+1)
        
        helperFunction(0)
        return answer