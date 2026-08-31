class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []

        # this method works, but it relies on the array being sorted
        nums.sort()
        
        for i in range(len(nums)):

            # trying to re-arrange i+j+k=0 into -i=(j+k)

            # skipping the index where i is 2 lesser than the len(nums), cant form
            if i+2>= len(nums):
                continue
            
            # if the value is the same as prev, then can skip to preent the same set being included
            elif i>=1 and nums[i]==nums[i-1]:
                continue

            # select the target, left and right
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            
            # using the two points to find all possible soluitions
            while right>left:
                
                sum_val = nums[left]+nums[right]

                # checking if the target has been found
                if target == sum_val :
                    answer.append([-target,nums[left], nums[right]])

                    # move the right and left
                    left+=1
                    right-=1

                    # checking for duplicate
                    while right>left and nums[left]==nums[left-1]:
                        left+=1

                elif sum_val>target:
                    right-=1
                else:
                    left+=1
            
        return answer