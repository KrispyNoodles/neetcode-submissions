class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])


        def dfs(r,c, visited):

            # checking for oob
            if min(r,c)<0 or r==ROW or c==COL:
                return 
            
            if (r,c) in visited:
                return
            
            # elsee add into visited
            visited.add((r,c))

            # replace with 0
            if grid[r][c]=="1":
                grid[r][c]="0"
            else:
                return
            
            # explore other places
            dfs(r+1,c, visited)
            dfs(r,c+1, visited)
            dfs(r,c-1, visited)
            dfs(r-1,c, visited)
        
        answer = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c]=='1':
                    answer+=1
                    dfs(r,c,set())

        return answer