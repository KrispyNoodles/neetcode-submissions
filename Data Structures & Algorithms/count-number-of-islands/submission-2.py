class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        counter = 0
        visited = set()

        ROW, COL = len(grid), len(grid[0])

         # island_counter
        def helperFn(r, c):

            # checking if r, c if empty
            if min(r,c)<0 or r==ROW or c==COL:
                return
            
            # checking if it is a 0 or it has been visited before
            if grid[r][c]=='0' or (r,c) in visited:
                return

            # checking if it is 1, then it can increment the counter and continue
            # then convert the 1 into 0
            if grid[r][c]=='1':
                grid[r][c]='0'
                visited.add((r,c))

            helperFn(r+1,c)
            helperFn(r-1,c)
            helperFn(r,c+1)
            helperFn(r,c-1)

        # getting the first 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                # when a 1 is found
                if grid[r][c] == '1':
                    counter+=1
                    helperFn(r,c)

        return counter