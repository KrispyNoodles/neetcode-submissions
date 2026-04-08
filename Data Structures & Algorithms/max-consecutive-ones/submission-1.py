class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        counter = 0
        highest_counter = 0

        for number in nums:
            if number==1:
                counter+=1
                highest_counter = max(counter, highest_counter)
                
            else:
                counter = 0

        return highest_counter