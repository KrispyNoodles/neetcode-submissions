class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # starting row and color

        # for each of the thingy that is the current color in the starting,
        # it will change to the new color
        ROW, COL = len(image), len(image[0])
        first_color = image[sr][sc]
        def helperFn(r, c):

            # checking for oob
            if r==ROW or c==COL or min(r,c)<0 or image[r][c]==color:
                return

            # checking current square
            if image[r][c]==first_color:
                image[r][c]=color

            else:
                return
            
            # exploring other places
            helperFn(r,c+1)
            helperFn(r+1,c)
            helperFn(r,c-1)
            helperFn(r-1,c)

        helperFn(sr, sc)
        return image