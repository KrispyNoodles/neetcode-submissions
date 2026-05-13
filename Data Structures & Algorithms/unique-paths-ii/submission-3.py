from typing import List

# Dynamic Programming, Bottom Up Programming
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        
        # vomit back out
        prevRow = [0]*COL

        # moving up the rows
        for r in range(ROW-1,-1,-1):

            currRow = [0]*COL

            # populating the values now in currRow
            # populate every value except the last one, because it has been populated above
            for c in range(COL-1,-1,-1):

                # checking if there is an obstacle
                if obstacleGrid[r][c]==1:
                    currRow[c] = 0

                # checking if it is the end
                elif r==ROW-1 and c==COL-1:
                    currRow[c] = 1

                else:
                    # ensuring that you dont access a value outside the number of cols
                    if c+1 <= COL-1:
                        # add the right side and add the bottom
                        currRow[c] = currRow[c+1] + prevRow[c]
                    else:
                        currRow[c] = prevRow[c]
                
            # replace the row
            prevRow = currRow

        # return the top left
        return prevRow[0]

        