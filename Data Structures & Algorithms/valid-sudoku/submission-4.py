from typing import List

# similar to mine but alot more optimised using a set instead of storing and checking in an array
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        # checking for all rows
        for row in range(9):

            # creating a new set for each row
            seen = set()

            for i in range(9):

                character = board[row][i]

                # add it to the board
                if character != '.':
                    # checking if it has appeared before
                    if character in seen:
                        return False
                    else:
                        seen.add(character)

        
        # checking for all cols
        for cols in range(9):

            # creating a new set for each cols
            seen = set()

            for i in range(9):

                character = board[i][cols]

                # add it to the board
                if character != '.':
                    # checking if it has appeared before
                    if character in seen:
                        return False
                    else:
                        seen.add(character)

        # checking for each square matrix (3 by 3)

        for square in range(9):
            seen = set()

            # incremeneting to 3 because its 3 by 3
            for i in range(3):
                for j in range(3):
                    
                    # the times 3 helps to shift the entire square 

                    # it divides by 3 and finds the value without remmainder
                    # so for the first square 0, it times 3 to shift across the rows and + i to increment across the 3 squares 
                    row = (square//3)*3 + i

                    # this gets the remmainder so that it moves across the cols
                    col = (square %3 )*3 +j

                    character = board[row][col]

                    # add it to the board
                    if character != '.':
                        # checking if it has appeared before
                        if character in seen:
                            return False
                        else:
                            seen.add(character)
        
        return True

