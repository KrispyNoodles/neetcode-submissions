# using set

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # looping throught the values of the matrix
        for arrays in matrix:

            # creating a temp set for each array
            temp_set = set(arrays)
            
            if target in temp_set:
                return True
        
        return False
