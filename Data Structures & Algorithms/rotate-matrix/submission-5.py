class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix)-1

        while r>l:

            for i in range(r-l):

                top, bottom = l, r

                # storing the top left
                # topleft shifts across the left variable
                temp = matrix[top][l+i]

                # bottom left replace with top left
                # moving the row indices move upawards (decrement)
                matrix[top][l+i] = matrix[bottom-i][l]
                
                # replace bottom left with bottom right
                # bottom right left along the col axis (decrement)
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # replace bottom right with top right
                # the top right moves down along the row axis (increment)
                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = temp

            
            l+=1
            r-=1
    


