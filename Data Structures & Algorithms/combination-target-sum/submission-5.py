class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = []
        current_set = []

        def helperFunction(i):

            # base cases
            if sum(current_set)==target:
                # add it into the answer
                answer.append(current_set.copy())
                return

            # if more than targe thten return
            if sum(current_set)>target:
                return
            
            # if the i more than the current len(nums) then reutrn
            if i>=len(nums):
                return 
            
            # else increment itself
            current_set.append(nums[i])
            helperFunction(i)

            # backtrack
            current_set.pop()
            helperFunction(i+1)
        
        helperFunction(0)
        return answer