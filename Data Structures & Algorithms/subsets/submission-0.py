class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if nums == []:
            return []

        master_set = []
        path = []
        
        def backtrack(start):

            # add into the answer
            master_set.append(path.copy())

            for i in range(start, len(nums)):
                # choose
                path.append(nums[i])

                # explore
                backtrack(i+1)

                # backtrack
                path.pop()

        backtrack(0)
        return master_set
            