class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # transpose then reverse each row
        for r in range(len(matrix)):
            # we are only doing the top triangle of it
            for c in range(r, len(matrix[0])):

                # switcheroo
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        for r in matrix:
            r.reverse()