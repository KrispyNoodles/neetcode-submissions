class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # using subset code first
        path = []
        master_set = []

        # reorder nums
        nums.sort()

        def helperFn(start):

            if path not in master_set:
                master_set.append(path.copy())

            for i in range(start, len(nums)):
                # select option
                path.append(nums[i])

                # explore
                helperFn(i+1)

                # backtrack
                path.pop()
        
        helperFn(0)

        return master_set