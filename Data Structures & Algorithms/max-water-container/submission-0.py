class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # 
        max_area = 0

        for left_index in range(len(heights)):

            # create dupe right side
            new_arr = heights.copy()

            # finding right
            for right_index in range(left_index+1, len(heights)):

                # calc area:
                area_tank = min(heights[left_index], heights[right_index])*(right_index-left_index)

                max_area = max(max_area, area_tank)

        return max_area