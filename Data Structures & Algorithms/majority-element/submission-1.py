class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        d= {}

        for n in nums:

            # count
            if n not in d:
                d[n]=1
            
            elif n in d:
                d[n]+=1

            # checking count
            if d[n]>=len(nums)/2:
                return n