class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # transpose amtrix
        # row become colum
        # columnw become row and then flip

        # just built new matrix?
        answer = []

        ROWS, COLS = len(matrix), len(matrix[0])

        for _ in range(COLS):
            answer.append([0]*ROWS)

        for r in range(ROWS):
            for c in range(COLS):
                answer[c][r] = matrix[r][c]
        
        return answer