class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while right>=left:

            middle = (right+left)//2

            if nums[middle]==target:
                return middle
            
            # checking if it in the left sorted
            if nums[middle]>=nums[left]:

                # checking if target is inside
                if target>nums[middle] or target<nums[left]:
                    # if not inside then search right
                    left = middle+1
                else:
                    right = middle-1
            else:
                # if not inside sorted right, search left
                if target<nums[middle] or target>nums[right]:
                    right = middle-1
                else:
                    left = middle+1
        
        return -1
                
