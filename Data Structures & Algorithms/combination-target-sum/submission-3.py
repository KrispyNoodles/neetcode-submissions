class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        path = []
        master_set = []

        def backtrackFn(start, target):

            if target == 0:
                master_set.append(path.copy())

            if target <0:
                return

            for i in range(start, len(nums)):

                # select
                path.append(nums[i])

                # explore
                backtrackFn(i, target-nums[i])

                # backtrack
                path.pop()

        backtrackFn(0, target)
        
        return master_set


