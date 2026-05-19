class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # can start from position 1 since position 0 is confirm to be not in before
        left = 1

        for i in range(1, len(nums)):

            # if the curr value is different from the prev value
            # write it in
            if nums[i] != nums[i-1]:
                
                # activate writer
                nums[left] = nums[i]
                left+=1
        
        return left