class Solution:
    # m is row and n is col
    def uniquePaths(self, m: int, n: int) -> int:
        
        # creating a prev row
        prevRow = [0]*n

        # moving from the height to -1 by -1
        for _ in range(m-1, -1, -1):

            # creating a current row
            curRow = [0]*n

            # the bottom right corner is a 1
            curRow[n-1] = 1

            # populating the curRow
            for c in range(n-2, -1, -1):

                # add the right and bottom
                curRow[c] = curRow[c+1] + prevRow[c]

            # update the row
            prevRow=curRow

        return prevRow[0]