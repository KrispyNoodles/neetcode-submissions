class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # transpose the matrix
        # for each row it becomes a col
        # We only need to process the diagonal and everything above/right of it so that we do not swap it back again
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                # switcheroo
                matrix[c][r],matrix[r][c] = matrix[r][c],matrix[c][r]
        

        # reversing the rows 
        for r in matrix:
            r.reverse()