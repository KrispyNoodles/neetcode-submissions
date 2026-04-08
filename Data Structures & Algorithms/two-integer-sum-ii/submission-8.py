class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        length_array = len(numbers)

        for index_1, value in enumerate(numbers):
            
            # value to find
            value_2 = target-value

            new_array = numbers[index_1+1:length_array]
            
            # use the bin_search to keep finding
            index_return = self.bin_search(new_array, value_2)
            
            if index_return != -1:
                index_2 = index_return + index_1 + 1
                return [index_1+1, index_2+1]           

    def bin_search(self, array_1, target_value):

        left = 0
        right = len(array_1)-1

        while right>=left:

            # cal middle
            middle = (right+left)//2

            # target found
            if array_1[middle] == target_value:
                return middle

            elif target_value>array_1[middle]:
                left = middle+1 
                
            else:
                right = middle-1 

        # if not inside will return -1
        return -1
