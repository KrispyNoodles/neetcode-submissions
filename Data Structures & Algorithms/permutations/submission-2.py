class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        master_set = []

        used = [0]*len(nums)

        path = []
        
        def helperFn(path, used):

            if len(path) == len(nums):
                master_set.append(path.copy())
                return

            for i in range(len(nums)):

                if used[i] == False:

                    used[i] = True
                    # select
                    path.append(nums[i])

                    # explore
                    helperFn(path, used)

                    # backtrack
                    path.pop()
                    used[i] = False
        
        helperFn(path, used)
        return master_set
