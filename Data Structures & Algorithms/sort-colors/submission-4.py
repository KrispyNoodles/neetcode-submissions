class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # left writer
        left = 0

        # bring all 0 in front
        for i in range(len(nums)):
            
            # for 0 values
            if nums[i] == 0:
                # swaperoo
                nums[left], nums[i] = nums[i], nums[left]
                left+=1

        one_writer = left
        for i in range(len(nums)):
            if nums[i] == 1:
                # swaperoo
                nums[one_writer], nums[i] = nums[i], nums[one_writer]
                one_writer+=1

        two_writer = one_writer
        for i in range(len(nums)):
            if nums[i] == 2:
                # swaperoo
                nums[two_writer], nums[i] = nums[i], nums[two_writer]
                two_writer+=1