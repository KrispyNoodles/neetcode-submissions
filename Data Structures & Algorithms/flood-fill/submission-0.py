from typing import List

class Solution:


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # geting the oriignal color
        original_color = image[sr][sc]
        visited=set()

        # using DFS
        ROWS, COLS = len(image), len(image[0])

        def helperFn(sr, sc, visited):          

            # checking for all scenerios where the pixel will not be filled
            # went negative or oob
            if min(sr, sc)<0 or sr==ROWS or sc==COLS or (sr,sc) in visited:
                print('nothing happens')
                return

            # went to a pixel that is the same as the starting pixel (therefore it does not need to change)
            if image[sr][sc]==original_color:
                visited.add((sr,sc))

                # update the image color
                image[sr][sc]=color

            # go back if the color is differnet
            else:
                return
                
            # exploration
            helperFn(sr+1, sc, visited)
            helperFn(sr-1, sc, visited)
            helperFn(sr, sc+1, visited)
            helperFn(sr, sc-1, visited)

            return
        
        helperFn(sr, sc, visited)

        return image
