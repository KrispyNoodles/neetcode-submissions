class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = []
        current_path = []

        def helperFn(i):

            # base cases
            if sum(current_path)==target:
                answer.append(current_path.copy())
                return

            # can stop exploring            
            if i>=len(nums):
                return

            if sum(current_path)>target:
                return
            
            current_path.append(nums[i])
            helperFn(i)

            current_path.pop()
            helperFn(i+1)

        helperFn(0)

        return answer
