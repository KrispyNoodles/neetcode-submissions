from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # the product will happen for all other values except for the value at the current index
        # if the current index's value is negative then the product answer is 0
        # get the total product, then divide by each of the value if it is positive
        
        answer = []

        for index in range(len(nums)):

            # duplicating the array
            temp_arr = nums[:]

            # remove the current index
            pop_val = temp_arr.pop(index)

            if pop_val == 0:
                product_val = self.product_arr(temp_arr)
                answer.append(product_val)

            else:
                # getting the prodcut value
                product_val = self.product_arr(temp_arr)
                answer.append(product_val)
            
        return answer

    def product_arr(self, list_of_nums):

        product_val = 1

        # if there is a 0 value then the product is 0
        if 0 in list_of_nums:
            return 0
        else:
            for value in list_of_nums:
                product_val = product_val*value

            return product_val
