class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # left and right of the matrix
        l, r = 0, len(matrix)-1

        while l<r:
            # because we only moving the length-1 number of times
            # on each i we move along the row of what is being rotate
            for i in range(r-l):
                top, bottom = l, r

                # save the top left value
                temp = matrix[top][l+i]

                # move the bottom left into the top left
                matrix[top][l+i] = matrix[bottom-i][l]

                # moving the bottom right into the bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # moving the top right into the bottom right 
                matrix[bottom][r-i] = matrix[top+i][r]

                # moving top left into top right (prev stored in tempv ar)
                matrix[top+i][r] = temp
            
            # updating left and right
            # because we are reducing the sides by 1 each
            r-=1
            l+=1