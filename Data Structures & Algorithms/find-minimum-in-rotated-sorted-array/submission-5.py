class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        answer = nums[0]
        left, right = 0, len(nums)-1

        while right>left:

            middle = (right+left)//2

            # checking if middle is the answer
            answer = min(answer, nums[middle])

            # search right
            if nums[middle]>=nums[right]:
                left = middle+1
                
            else:
                right=middle
                
            answer = min(answer, nums[left])

        return answer
