class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # creating a dict
        dic = {}

        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
            
        if len(dic)!=len(nums):
            return True
        else:
            return False