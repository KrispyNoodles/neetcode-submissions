from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        path = []
        master_set = []

        def helperFn(start, target):

            if target==0:
                print('target is found')
                master_set.append(path.copy())
            
            # if it does not work, it should return immediately
            if target<0:
                return 
            
            for i in range(start, len(nums)):
                
                # selecting an option
                path.append(nums[i])

                # reselecting the same option
                helperFn(i, target-nums[i])

                # poping back
                path.pop()

        helperFn(0, target)

        return master_set