class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort the array
        nums.sort()

        answer = []

        # for each value in the nums, it takes a chance to be the target
        for i in range(len(nums)):

            # target
            # reframing into -nums[i] = nums[j] + nums[k]
            target = -nums[i]

            # checking for results that are invalid
            if i+2>len(nums):
                continue
            
            # if i and the value before is the same
            elif i>=1 and nums[i]==nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            # two pointer soln
            while right>left:

                sum_val = nums[left] + nums[right]

                if sum_val == target:
                    answer.append([-target, nums[left], nums[right]])
                
                    left+=1
                    right-=1

                    # shift the left is the val is the same
                    while right>left and nums[left]==nums[left-1]:
                        left+=1
                elif sum_val>target:
                    right-=1

                else:
                    left+=1
        
        return answer

            
