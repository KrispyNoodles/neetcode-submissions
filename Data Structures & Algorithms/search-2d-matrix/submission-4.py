# searh using a single bin search

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_row = len(matrix)
        matrix_col = len(matrix[0])

        # looping through the values of the matrix
        left = 0
        right = (matrix_row*matrix_col)-1

        while right >= left:

            middle = (right+left)//2

            row = middle // matrix_col
            col = middle % matrix_col

            if matrix[row][col] > target:
                right = middle-1

            elif matrix[row][col] < target:
                left = middle+1

            else:
                return True

        return False
            
# time compelxity of O(log(n*m)) where n is the number of rows and m is the number of columns