class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # for every rectangle, move to the left and right and see what is the biggest area you can create
        maximum_area = 0 
        max_index = len(heights)

        # function that calcs the area
        def helperFn(rect_index, rect_height):            

            # calc left_side, find the minimum height then area
            left_array = heights[0:rect_index]
            left_array = left_array[::-1]

            rect_length = 0

            for i in left_array:
                if i >= rect_height:
                    rect_length+=1
                else:
                    break
            
            ## Right calculations
            right_array = heights[rect_index:max_index]

            for i in right_array:
                if i >= rect_height:
                    rect_length+=1
                else:
                    break
            
            rect_area = rect_length*rect_height

            # how far left can move and how far right can move
            return rect_area

        for index, rectangle in enumerate(heights):
            maximum_area = max(maximum_area, helperFn(index, rectangle))
        
        return maximum_area
