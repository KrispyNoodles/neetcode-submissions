from typing import List

# using binary search to return the one on the right
# because the number list is already sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index_1, value in enumerate(numbers):
            index_2 = self.bin_search(numbers, target-value)

            if index_2 != -1:
                
                # making it 1 index
                return [index_1+1, index_2+1]

    
    def bin_search(self, numbers, val_to_find):
        right = len(numbers)-1
        left = 0

        while right>=left:
            middle = (right+left)//2

            if val_to_find==numbers[middle]:
                return middle

            elif val_to_find<numbers[middle]:
                right = middle-1
            else:
                left = middle+1
        
        return -1