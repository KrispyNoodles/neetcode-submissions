from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        master_set = []
        path = []

        # this sort ensures that the duplicates look the same
        nums.sort()

        # start is an index
        def helperFn(start):
            
            # this part, seperates Subsets II from I 
            if path not in master_set:
                master_set.append(path.copy())


            for i in range(start, len(nums)):

                # select path
                path.append(nums[i])

                # explore other path
                helperFn(i+1)

                # backtrack
                path.pop()

        helperFn(0)

        return master_set

# time compleexity of O(n*n^2)