class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        path = []
        master_set = []
        
        def helperFn(start, target_var):

            # adding the path into the answer if it fulfils
            if target_var == 0:
                master_set.append(path.copy())

            # it means it has added over
            elif target_var<0:
                return
            
            for i in range(start, len(nums)):
                # select option
                path.append(nums[i])

                # exploring option, with adjusted target
                helperFn(i, target_var-nums[i])

                path.pop()

        
        helperFn(0, target)
        return master_set