class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1

        max_left = height[left]
        max_right = height[right]

        answer = 0

        while right>left:

            # if right is bigger, it means the water 
            # for sure can be trapped on the left side

            if height[right]>height[left]:
                left+=1
                # update the max height
                max_left = max(max_left, height[left])
                answer+= max_left-height[left]
                
            
            else:
                right-=1
                # update the max height
                max_right = max(max_right, height[right])
                answer+= max_right-height[right]
                
        return answer

# time complexity of O(n)