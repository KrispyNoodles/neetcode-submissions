class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        left = 0
        right = len(heights)-1

        while right>left:

            # for every movement lets check the area
            area = (right-left)*min(heights[left], heights[right])
            max_area = max(area, max_area)

            # seeing which length is smaller, then move it
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        
        return max_area