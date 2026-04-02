from typing import List

# re-attempt

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # the product will happen for all other values except for the value at the current index
        # if the current index's value is negative then the product answer is 0
        # get the total product, then divide by each of the value if it is positive
        
        # creating an array of 0
        answer = [0]*len(nums)

        # finding the indexes of 0
        zero_indexes = []


        product_val = 1

        # calculating the value without 0
        for index in range(len(nums)):
            if nums[index] != 0:
                product_val = product_val*nums[index]
            else:
                zero_indexes.append(index)
        
        # if there are more than 1 zeros, it means the entire product is alway 0
        if len(zero_indexes)>1:
            return answer
        
        # everything is 0 except for the value at the zero_index
        elif len(zero_indexes)==1:
            answer[zero_indexes[0]]=product_val
            return answer

        # there is no zero value
        else:
            # divide all the product to the vlaue at the index
            for index in range(len(nums)):
                answer[index] = product_val//nums[index]
            return answer
