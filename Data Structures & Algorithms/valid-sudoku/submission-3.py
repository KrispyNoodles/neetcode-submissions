from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        # Only the filled cells need to be validated according to the mentioned rules.

        check = True
                
        # checking for duplicate in columns
        # converting rows to col
        
        temp_2d_array = []
        
        for index in range(len(board)):
            temp_col = []

            for rows in board:
                temp_col.append(rows[index])

            temp_2d_array.append(temp_col)

        # checking for rows
        check = self.row_checker(board)

        if check == False:
            return False

        # rotate board to check for rows again
        check = self.row_checker(temp_2d_array)

        if check==False:
            return False

        # the checks so far is just for rows, but we need to check in the grid of 9 (3 by 3)
        # 1, 2, 3
        # 4, 5, 6
        # 7, 8, 9
        
        # used for checking
        single_temp_array = []
        
        # checking for 3 by 3 grids on first row
        row_index = 0

        while row_index < len(board):
            col_index = 0

            while col_index < len(board):

                # new temp_array everytime
                single_temp_array = []
                row_counter = 0
                
                while row_counter < 3:
                    col_counter = 0
                    
                    # appending the values in the 3 by 3 array
                    while col_counter < 3:

                        # print(f"row is {row_counter}")
                        # print(f"col is {col_counter+index}")

                        if board[row_counter+row_index][col_counter+col_index].isdigit():
                            single_temp_array.append(board[row_counter+row_index][col_counter+col_index])

                        # move column by 1
                        col_counter+=1

                    # move row by 1 after all the columns are done
                    row_counter+=1
                
                # print(single_temp_array)
                # checking if there are unique values
                if len(single_temp_array) > len(set(single_temp_array)):
                    return False
                
                # move by 3
                col_index += 3
            
            row_index += 3

            return check
    
    def row_checker(self, board):

        # checking for duplicate in rows
        for rows in board:

            temp_row = []
        
            # removing all the dots in the row
            for value in rows:
                if value.isdigit():
                    temp_row.append(value)

            # this means there is a repeated element
            if len(temp_row) > len(set(temp_row)):
                return False
        
        return True
