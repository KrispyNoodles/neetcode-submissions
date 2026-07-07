class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # using binary search

        # def ans
        answer = nums[0]

        left,right = 0, len(nums)-1

        while right>left:
            # getting middle
            middle = (right+left)//2

            # new answer
            answer = min(answer,nums[middle])

            # this means that we just search on the right
            if nums[middle]>=nums[right]:
                
                left = middle+1
                # search left, left most is the answer
                answer = min(answer, nums[left])

            else:
                # search left
                # middle +1 is the answer
                right = middle-1

                answer = min(answer, nums[left])

        return answer