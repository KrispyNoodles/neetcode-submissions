class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        left = 0
        right = 1

        if len(nums)==1:
            return True

        while right<len(nums):

            left_val = nums[left]
            right_val = nums[right]

            if left_val%2==0 and right_val%2==1:
                left+=1
                right+=1
                continue
            if right_val%2==0 and left_val%2==1:
                left+=1
                right+=1
                continue
            else:
                return False

            left+=1
            right+=1
        
        return True