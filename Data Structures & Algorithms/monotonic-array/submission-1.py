class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        mono_decrease = False
        mono_increase = False
        
        # checking how long is len(nums)
        if len(nums)>=2:

            # check if it is increasing or decreasing
            if nums[0] >= nums[-1]:

                # if the first element is biggest than the element at the end
                # decreasing supposedly
                mono_decrease = True
            
            else:
                mono_increase = True

        # only have one element
        else:
            return True

        for i in range(0, len(nums)-1):

            # checking if the next eelment is bigger than the current
            if mono_increase:
                if nums[i+1]>=nums[i]:
                    continue
                else:
                    return False

            if mono_decrease:
                if nums[i+1]<=nums[i]:
                    continue
                else:
                    return False
        
        return True