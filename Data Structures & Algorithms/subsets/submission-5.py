class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        current_set = []

        def helperFn(i):

            if i>=len(nums):
                answer.append(current_set.copy())
                return

            # adding in the i into the current_set
            current_set.append(nums[i])
            helperFn(i+1)

            # reverse back
            current_set.pop()
            helperFn(i+1)
        
        helperFn(0)

        return answer