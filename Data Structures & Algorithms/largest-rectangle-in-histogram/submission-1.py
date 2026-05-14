class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # for every rectangle, move to the left and right and see what is the biggest area you can create
        maximum_area = 0 

        # function that calcs the area
        def helperFn(rect_index, rect_height):

            left_index = 0
            right_index = len(heights)

            # calc left_side, find the minimum height then area
            left_array = heights[0:rect_index]
            left_array = left_array[::-1]

            left_length = 0

            for i in left_array:
                if i >= rect_height:
                    left_length+=1
                else:
                    break
            
            left_area = left_length*rect_height

            ## Right calculations
            right_array = heights[rect_index:right_index]

            right_length = 0

            for i in right_array:
                if i >= rect_height:
                    right_length+=1
                else:
                    break
            
            right_area = right_length*rect_height

            # how far left can move and how far right can move
            return left_area + right_area

        for index, rectangle in enumerate(heights):
            maximum_area = max(maximum_area, helperFn(index, rectangle))
        
        return maximum_area
        
