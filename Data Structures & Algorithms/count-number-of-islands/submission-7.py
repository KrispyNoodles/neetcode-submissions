class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        # whenever it reaches an island move around all the squares and covnert it into water
        answer = 0 
        ROWS, COLS = len(grid), len(grid[0])

        # we want to explore all options so it is using bfs
        def bfs(r,c, visited):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return
            
            if (r,c) in visited:
                return
            
            # else check if it is a 1 or 0
            if grid[r][c]=="1":
                # convert it into 0
                grid[r][c]="0"

            else:
                return

            # add the point into visited
            visited.add((r,c))

            # explore all the options
            bfs(r+1,c, visited)
            bfs(r,c+1, visited)
            bfs(r-1,c, visited)
            bfs(r,c-1, visited)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    answer+=1
                    bfs(r,c, set())


        return answer


