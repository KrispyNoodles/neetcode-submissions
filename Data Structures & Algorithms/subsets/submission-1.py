class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        master_set = []

        def helperFn(start):

            # add the current path into the master_set
            master_set.append(path.copy())

            for i in range(start, len(nums)):

                # select option
                path.append(nums[i])

                # explore other options
                helperFn(i+1)

                # backtrack
                path.pop()


        helperFn(0)

        return master_set

