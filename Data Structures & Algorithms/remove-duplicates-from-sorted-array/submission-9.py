# Faast and slow method

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        total_len = len(nums)
        slow, fast = 0, 1

        while fast < total_len:

            # checking if the swap should be done
            if nums[slow] != nums[fast]:

                # placing it in the next position
                nums[slow+1]=nums[fast]
                # move both pointer
                slow+=1
                fast+=1
            else:
                # move fast only 
                fast+=1
        
        return slow+1