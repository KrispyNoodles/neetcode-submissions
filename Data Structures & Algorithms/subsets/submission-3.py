class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        master_set = []
        path = []

        def backtrackFn(start):

            # append the path into the master_set
            master_set.append(path.copy())

            for i in range(start, len(nums)):

                # select option
                path.append(nums[i])

                # explore other
                backtrackFn(i+1)

                # backtrack
                path.pop()

        
        backtrackFn(0)

        return master_set