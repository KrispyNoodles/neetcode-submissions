from typing import List

class Solution:


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # geting the oriignal color
        original_color = image[sr][sc]

        # using DFS
        ROWS, COLS = len(image), len(image[0])

        def helperFn(sr, sc):          

            # checking for all scenerios where the pixel will not be filled
            # went negative or oob
            if min(sr, sc)<0 or sr==ROWS or sc==COLS:
                print('nothing happens')
                return
            
            # if the color is the same as the color that needs to be change, skip
            # then you dont need the visited
            if image[sr][sc]==color:
                return

            # went to a pixel that is the same as the starting pixel (therefore it does not need to change)
            if image[sr][sc]==original_color:

                # update the image color
                image[sr][sc]=color

            # go back if the color is differnet
            else:
                return
                
            # exploration
            helperFn(sr+1, sc)
            helperFn(sr-1, sc)
            helperFn(sr, sc+1)
            helperFn(sr, sc-1)

            return
        
        helperFn(sr, sc)

        return image
