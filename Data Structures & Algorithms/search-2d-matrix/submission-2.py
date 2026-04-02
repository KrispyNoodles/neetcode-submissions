# using set

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # looping throught the values of the matrix
        for arrays in matrix:

            if target in arrays:
                return True
        
        return False

# time compelxity of O(n*m) where n is the number of rows and m is the number of columns