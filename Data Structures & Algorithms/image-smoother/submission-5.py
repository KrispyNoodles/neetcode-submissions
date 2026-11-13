class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass

        # creating a new matrix
        ROWS, COLS = len(img), len(img[0])
        new_matrix = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):

                # creating a box and retrieivn the total sum and the number of elements
                counter = 0
                total_sum = 0

                # smallest have to be 0 anad biggest have to be rows, since it will be to rows-1
                # have to be +2 because we want to reach +1
                for j in range(max(r-1, 0), min(r+2, ROWS)):
                    for k in range(max(c-1, 0), min(c+2, COLS)):

                        # increment and counting
                        counter+=1
                        total_sum+=img[j][k]
                
                # average for each value
                new_matrix[r][c] = total_sum//counter

        return new_matrix