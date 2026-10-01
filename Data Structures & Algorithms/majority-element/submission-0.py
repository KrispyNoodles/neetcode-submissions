class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # create a dict
        d = {}

        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        
        # sort
        ans = sorted(d.items(), key=lambda x: x[1], reverse=True)

        key, count = ans[0]

        return key

