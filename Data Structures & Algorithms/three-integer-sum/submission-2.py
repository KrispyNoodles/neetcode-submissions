class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort it first
        nums.sort()

        answer = []

        # making each input in nums the target
        for i in range(len(nums)):

            target = -nums[i]
            left = i+1
            right = len(nums)-1

            # checking if have valid triplet
            if i+2>len(nums):
                continue
            
            # checking for situation where the target is repeataed twice
            if i>=1 and nums[i]==nums[i-1]:
                continue

            while right>left:

                sum_val = nums[left]+nums[right]

                if sum_val==target:
                    answer.append([-target, nums[left], nums[right]])

                    right-=1
                    left+=1

                    while right>left and nums[left]==nums[left-1]:
                        left+=1

                elif sum_val>target:
                    right-=1
                
                else:
                    left+=1
        
        return answer