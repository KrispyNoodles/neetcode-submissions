class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass

        ROWS, COLS = len(img), len(img[0])

        answer = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):

                # for each value we calc a grid around it and take the average
                counter = 0
                sum_val = 0

                for i in range(max(0, r-1), min(ROWS, r+2)):
                    for j in range(max(0, c-1), min(COLS, c+2)):
                        counter+=1
                        sum_val+=img[i][j]

                
                # add he value in
                answer[r][c]=sum_val//counter

        return answer