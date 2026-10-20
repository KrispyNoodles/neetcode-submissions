class Solution:
    def specialArray(self, nums: List[int]) -> int:
        

        # each takes a turn to be special
        for i in range(1, len(nums)+1):
            counter = 0
            # counting now
            for num in nums:
                if num>=i:
                    counter+=1            
            # check if counter == i +1
            if counter == i:
                return counter
        
        return -1
