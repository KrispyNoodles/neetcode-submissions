class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        # create helper Function
        def helperFn(sr, sc):

            # checking for oob
            if min(sr,sc)<0 or sr==ROWS or sc==COLS:
                return
            
            # if it is already the same color, can just ignore
            if image[sr][sc]==color:
                return

            # if it is a valid color, update
            if image[sr][sc]==original_color:
                image[sr][sc]=color
                
            # else return
            else:
                return

            helperFn(sr,sc+1)
            helperFn(sr,sc-1)
            helperFn(sr+1,sc)
            helperFn(sr-1,sc)

        helperFn(sr,sc)

        return image