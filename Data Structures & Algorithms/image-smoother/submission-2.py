class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass

        # get row and col
        ROWS, COLS = len(img), len(img[0])

        # work with the square
        answer = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):

                total = 0
                count = 0

                # creating the 3 by 3 grid
                # +2 because range exludes iterating through the last value
                for x in range(max(0,r-1), min(ROWS, r+2)):
                    for y in range(max(0,c-1), min(COLS, c+2)):

                        total+=img[x][y]
                        count+=1
                
                answer[r][c]= total//count

        return answer