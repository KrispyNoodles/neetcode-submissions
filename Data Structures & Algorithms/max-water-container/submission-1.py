class Solution:
    def maxArea(self, heights: List[int]) -> int:


        max_area = 0
        
        # using two pointers
        left, right = 0, len(heights)-1

        # we always move the shorter among the left and right side
        # because we want to have the widest as much as possible

        while right>left:

            # calc area
            area = min(heights[left], heights[right])*(right-left)

            # do area comparison
            max_area = max(area, max_area)
            
            # if the left side is taller, then reduce the right side
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1

        return max_area