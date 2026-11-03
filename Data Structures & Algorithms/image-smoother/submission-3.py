class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass

        ROWS, COLS = len(img), len(img[0])

        # create new image
        new_image = [[0]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                
                summer = 0 
                counter = 0

                # for each pixel
                # -1 to +2
                for i in range(max(0, r-1), min(ROWS, r+2)):
                    for j in range(max(0, c-1), min(COLS, c+2)):

                        

                        summer+=img[i][j]
                        counter+=1
                
                new_image[r][c]=summer//counter

        return new_image
                    

