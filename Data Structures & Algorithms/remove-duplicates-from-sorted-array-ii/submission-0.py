class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # writer
        left = 2

        for i in range(2, len(nums)):

            # checking if only one same
            if nums[i]!=nums[left-2]:
                
                nums[left] = nums[i]
                left+=1
            
            # both are the same a
            else:
                nums[left] = nums[i]

 
        print(nums)
        return left