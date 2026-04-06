from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index_1, number in enumerate(numbers):

            value_to_find = target-number
    
            # checking if the number is inside
            # and the number is not the same
            if value_to_find in numbers:

                # pop it and find
                numbers.pop(index_1)
                
                # +1 because it pop the element earlier
                index_2 = numbers.index(value_to_find) + 1

                # add 1 because of 1-index
                return [index_1+1, index_2+1]
            