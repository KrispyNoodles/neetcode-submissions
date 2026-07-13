class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        current_set = []

        def helperFn(i):

            if i>=len(nums):
                answer.append(current_set.copy())
                return
            
            current_set.append(nums[i])
            helperFn(i+1)

            current_set.pop()
            helperFn(i+1)

        helperFn(0)

        return answer