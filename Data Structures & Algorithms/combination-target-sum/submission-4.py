class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # using the same method as the subsets to solve
        answer = []
        current_path = []

        def helperFn(i):
            
            # if the current_path == target then add into answer
            if sum(current_path)==target:
                answer.append(current_path.copy())
                return 
            
            # if the current path is more than the target return
            if sum(current_path)>target:
                return
            
            # if index outside then return
            if i>=len(nums):
                return
            
            # adding it in
            current_path.append(nums[i])
            helperFn(i)

            current_path.pop()
            helperFn(i+1)
        
        helperFn(0)

        return answer
