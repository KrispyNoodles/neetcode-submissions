class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        # creating a dfs to replace all values in the island to be a water
        def dfs(r,c,visited):

            # checking for oob
            if min(r,c)<0 or r==ROWS or c==COLS:
                return

            if grid[r][c]=="0":
                return
            else:
                grid[r][c]="0"

            if (r,c) in visited:
                return

            # include in the visits
            visited.add((r,c))
            
            # explore others
            dfs(r-1,c,visited)
            dfs(r+1,c,visited)
            dfs(r,c-1,visited)
            dfs(r,c+1,visited)

        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    answer+=1
                    dfs(r,c,set())

        return answer
