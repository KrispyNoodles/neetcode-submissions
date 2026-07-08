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
                
                # if the sorted left is bigger than the right
                # or if the right (which is alrdy is the biggest in the sort) is smaller than the value

                # then search right
                if nums[left]>target or target>nums[middle]:

                    # check right
                    left = middle+1

                # else we should check left
                else:
                    right = middle-1

            # we are in the right sorted portion
            else:

                # if the target is smaller than the middle value
                # OR if it is bigger than the right value
                if target<nums[middle] or target>nums[right]:
                    # search left
                    right = middle-1

                # else we continue searching the right
                else:
                    left = middle+1

        # this means the target isnt found
        return -1