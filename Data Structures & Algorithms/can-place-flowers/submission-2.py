class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        pointer = 0
    
        while pointer < len(flowerbed):
            
            # if there is a flower move
            if flowerbed[pointer]==1:
                pointer+=1
            
            else:

                left_empty = False
                right_empty = False

                # check if the left is emtpy
                if flowerbed[pointer-1]==0 or pointer==0:
                    left_empty = True

                # the left assignment checks before the error of index out of range is flagged
                if pointer==len(flowerbed)-1 or flowerbed[pointer+1]==0:
                    right_empty = True

                if left_empty and right_empty:
                    n-=1
                    flowerbed[pointer]=1
                
                # move the pointer no matter what
                pointer+=1
                
               

        if n<=0:
            return True
        else:
            return False
