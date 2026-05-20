class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        # creating a row addition
        # either row or col is needed
        self.prefix_row = []

        for r in range(len(matrix)):
            temp_arr_row = []

            row_sum = 0

            for c in range(len(matrix[0])):
                row_sum+=matrix[r][c]

                temp_arr_row.append(row_sum)

            self.prefix_row.append(temp_arr_row)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        answer = 0

        for i in range(row1, row2+1):

            left_sum = self.prefix_row[i][col1-1] if col1 >0 else 0
            right_sum = self.prefix_row[i][col2]
            answer += (right_sum-left_sum)
                
        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)