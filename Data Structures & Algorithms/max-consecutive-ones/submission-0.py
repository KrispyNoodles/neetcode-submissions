class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        counter = 0
        highest_counter = 0
        for number in nums:
            print(highest_counter)

            if number==1:
                counter+=1
            else:
                # retreive max then counter reset (if not it will be 0 compare with 0)
                highest_counter = max(counter, highest_counter)
                counter = 0

        # checking one more time
        highest_counter = max(counter, highest_counter)
        
        return highest_counter