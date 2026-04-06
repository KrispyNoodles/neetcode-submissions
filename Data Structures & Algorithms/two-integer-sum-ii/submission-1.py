from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for number in numbers:

            value_to_find = target-number
    
            # checking if the number is inside
            # and the number is not the same
            if value_to_find in numbers and (number != value_to_find):

                # find the index
                index_1 = numbers.index(number)
                index_2 = numbers.index(value_to_find)

                # print(index_1)

                # add 1 because of 1-index
                return [index_1+1, index_2+1]
            