class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        row, cols = len(image), len(image[0])

        def helperFn(sr, sc):

            # checking if it even exists
            if min(sr, sc)<0 or sr == row or sc ==cols or image[sr][sc] == color:
                return

            if image[sr][sc] == original_color:

                #change it
                image[sr][sc] = color
                
            else:
                return
            
            # exploring other spaces
            helperFn(sr+1,sc)
            helperFn(sr-1,sc)
            helperFn(sr,sc+1)
            helperFn(sr,sc-1)

        helperFn(sr, sc)

        return image