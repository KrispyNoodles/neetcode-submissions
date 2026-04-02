from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # looping throught the values of the matrix
        for arrays in matrix:
            answer = self.bin_search(arrays, target)

            if answer == True:
                return True
        
        return False
    
    def bin_search(self, array_1, target):

        left = 0
        right = len(array_1)-1

        while right>=left:

            middle = (right+left)//2

            # this means the target is on the left side
            if array_1[middle] > target:
                right = middle-1
            elif array_1[middle] < target:
                left = middle+1

            # middle is found
            else:
                return True

        return False