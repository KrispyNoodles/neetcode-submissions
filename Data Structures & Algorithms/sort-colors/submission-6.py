class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # low points to the next spot for 0
        low = 0

        curr = 0

        # high points to the next spot for 2
        high = len(nums)-1

        # curr must be below high, because high is where all the 2's value starts
        while curr<=high:
            
            # for 0 values
            if nums[curr] == 0:
                # swaperoo
                nums[low], nums[curr] = nums[curr], nums[low]
                low+=1
                curr+=1

            # for 2 values
            elif nums[curr] == 2:
                # swaperoo
                nums[high], nums[curr] = nums[curr], nums[high]
                high-=1

            else:
                curr+=1
        print(nums)
