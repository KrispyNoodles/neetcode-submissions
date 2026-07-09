class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while right>=left:

            # checking if it belongs to left or right
            middle = (right+left)//2

            # hcekcing if middle is answer
            if nums[middle]==target:
                return middle
            
            # checking if it the middle is on the sorted left
            if nums[middle]>=nums[left]:

                # checking if the target is not in the sorted left
                if target<nums[left] or target>nums[middle]:
                    left = middle+1
                else:
                    # this means it is within the left range
                    right = middle-1
            
            else:
                # checking if the target is not in the sorted right
                if target<nums[middle] or target>nums[right]:
                    right = middle-1
                else:
                    # this means it is within the left range
                    left = middle+1

        # after everything means it does not exist
        return -1