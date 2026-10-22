class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass

        ROWS, COLS = len(img), len(img[0])

        answer = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total =0
                count = 0
                # moving across the 3 by 3 grid
                # +2 because last index isnt included
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):

                        # if oobs get OUT
                        if min(i,j)<0 or i==ROWS or j==COLS:
                            continue
                        else:
                            total+=img[i][j]
                            count+=1
                
                answer[r][c] = total//count
        return answer