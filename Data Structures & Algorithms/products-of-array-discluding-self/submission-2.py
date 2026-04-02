from typing import List

# re-attempt

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # intuiton
        # [1,2,3,4]
        # product of values of the left of the index (prefix)
        # prefix = [1, 1, 1*2, 1*2*3] = [1, 1, 2, 6]

        # product of values of the right of the index (postfix)
        # postfix = [2*3*4, 3*4, 4, 1] = [24, 12, 4, 1]

        # final product if the value of index's predic * postfix

        
        # creating an array of 0
        answer = [0]*len(nums)

        # creating prefix
        prefix = [1]*len(nums)

        # ignore the first value
        for index in range(1, len(nums)):
            # the value in the prefix before * the value before the current index
            prefix[index] = prefix[index-1] * nums[index-1]


        # creating prefix
        postfix = [1]*len(nums)
        
        # ignore the first value
        for index in range(len(nums)-2, -1, -1):
            print(index)
            
            # the value in the postfix after * the value after the current index
            postfix[index] = postfix[index+1] * nums[index+1]
        

        # creating answer
        for index in range(len(nums)):
            answer[index] = prefix[index] * postfix[index]

        return answer

# time compuation is O(n) too since there is only one for loop the most