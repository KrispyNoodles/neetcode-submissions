class Solution:
    def search(self, nums: List[int], target: int) -> int:
                
        left, right = 0, len(nums)-1

        while right>=left:
            # check if the target is greater than the middle or not
            middle = (right+left)//2

            if nums[middle]==target:
                return middle
            
            # checking if the middle value belongs to the left side, which will be sorted
            if nums[middle]>=nums[left]:

                # now we see our target value if it belongs to the left or the right side
                
                # if the target value is bigger than the left and smaller than the middle,
                # we should check the left 
                if target>=nums[left] and nums[middle]>=target:

                    # check left
                    right = middle-1

                # else we should check right
                else:
                    left = middle+1

            # we are in the right sorted portion
            else:

                # we need to check if the target value is bigger than the middle and the right is bigger than the target
                # then that means we need search right side already
                if target>=nums[middle] and target<=nums[right]:
                    left = middle+1

                # else we continue searching the left
                else:
                    right = middle-1

        # this means the target isnt found
        return -1