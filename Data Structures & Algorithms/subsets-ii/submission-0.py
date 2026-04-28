class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        master_set = []
        path = []

        nums.sort()

        # start is an index
        def helperFn(start):

            if path in master_set:
                print("already isnide bro")

            else:
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
        





        