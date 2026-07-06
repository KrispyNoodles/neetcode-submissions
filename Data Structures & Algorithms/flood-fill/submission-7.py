class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])

        # starting pixel
        s_pixel = image[sr][sc]

        def helperFn(r,c):
            # checking if it is oob
            if min(r,c)<0 or r>=ROWS or c>=COLS or image[r][c]==color:
                return
            
            # checking if it is not the correct pixel
            if image[r][c]==s_pixel:

                # change the color, and explore
                image[r][c]=color

            else:
                return

            # else explore the other
            helperFn(r+1,c)
            helperFn(r,c+1)
            helperFn(r-1,c)
            helperFn(r,c-1)
        
        helperFn(sr,sc)

        return image