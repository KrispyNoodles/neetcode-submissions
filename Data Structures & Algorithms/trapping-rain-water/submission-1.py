class Solution:
    def trap(self, height: List[int]) -> int:
        
        # function that cals area

        # area = min(left_bar, right_bar)- values in between
        total_water = 0 

        # formula to calculate area at each point is
        # min(height[left], height[right]-height[i])

        for curr in range(len(height)):

            max_left_height, max_right_height = 0, 0

            # for each wall determine the highest wall on the left, 
            # and the next highest wall on the right

            # moving from left side of current point to 0, to the left
            for l in range(curr-1,-1,-1):
                # finding the tallest on the left side
                max_left_height = max(max_left_height, height[l])

            # movingfrom current point to the right
            for r in range(curr+1,len(height)):
                max_right_height = max(max_right_height, height[r])

            # water trap calc
            water_to_add = min(max_left_height, max_right_height)-height[curr]

            if water_to_add>0:
                total_water+=water_to_add

        return total_water
