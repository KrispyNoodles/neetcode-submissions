from typing import List

# using binary search to return the one on the right
# because the number list is already sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        length_arr = len(numbers)

        for index_1, value in enumerate(numbers):

            temp_array = numbers[index_1+1:length_arr]
            index_2 = self.bin_search(temp_array, target-value)

            if index_2 != -1:

                # add the index_2 to how much it has shifted
                index_2 += index_1+1
                
                # making it 1 index
                return [index_1+1, index_2+1]

    
    def bin_search(self, range, val_to_find):
        right = len(range)-1
        left = 0

        while right>=left:
            middle = (right+left)//2

            if val_to_find==range[middle]:
                return middle

            elif val_to_find<range[middle]:
                right = middle-1
            else:
                left = middle+1
        
        return -1