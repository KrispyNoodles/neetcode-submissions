class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums)<3:
            return []

        answer = []
        nums.sort()

        # each value in the nums becomes the soln to be found
        
        for index, value in enumerate(nums):
            
            # if index is second last then return
            # because wont have such possible answer
            if index == len(nums)-2:
                continue

            # if current element same as prev, then skip
            if index>0 and value==nums[index-1]:
                continue

            # start from the right of the value to the end
            left = index+1
            right = len(nums)-1

            # general forumla
            # -value = nums[left]+nums[right]
            while right>left:

                # if answer found add to answer
                if -value == nums[left]+nums[right]:
                    answer.append([value, nums[left], nums[right]])

                    # skip the element
                    while right>left and nums[left]==nums[left+1]:
                        left+=1

                    while right>left and nums[right]==nums[right-1]:
                        right-=1

                # if the sum is bigger than the value
                # then we should move the right to the left index
                if (nums[left]+nums[right])>(-value):
                    right-=1
                else:
                    left+=1

        return answer
