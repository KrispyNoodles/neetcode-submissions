class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # sort
        nums.sort()

        i=0
        print(nums)

        while i < (len(nums)-1):
            print(nums[i])

            if nums[i]==nums[i+1]:
                
                i+=2
            else:
                return nums[i]

        # return the last value
        return nums[i]