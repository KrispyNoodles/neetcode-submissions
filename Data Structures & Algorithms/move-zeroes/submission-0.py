class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # shifting the zero to the end
        left = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[left] = nums[i]
                left+=1
        
        # but this does not move the 0

        while len(nums)>left:
            nums[left]=0
            left+=1
        
        print(nums)
