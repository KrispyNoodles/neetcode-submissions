class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # for x in possible range of values
        for x in range(len(nums)+1):
            counter = 0
            
            # find how many values are bigger than nums
            for num in nums:
                if num>=x:
                    counter+=1
            
            # if the counter is the same as x
            if counter == x:
                return counter

        return -1