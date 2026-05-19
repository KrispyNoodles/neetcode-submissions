class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # sort it first
        nums.sort()

        # general formulae is
        # nums[i] + nums[j] + nums[k] == 0
        # same as -nums[i] == nums[j] + nums[k]

        answer = []

        for i in range(len(nums)):

            # if the current value is the same as the previous, can skip this round
            # as it would have found a subset of the previous one
            if i >0 and nums[i]==nums[i-1]:
                continue

            # the current target to find is 
            curr_target = -nums[i]

            # searching on the right side of the current target to find
            left, right = i+1, len(nums)-1

            # doing the 2 pointer search
            while right>left:
                
                sum_val = nums[left] + nums[right]

                if curr_target==sum_val:
                    answer.append([-curr_target, nums[left], nums[right]])

                    # because when the left or right value is shifted,
                    # if they were to view a same value again the same triplet will be created
                    
                    # the idea is to increment till it is different
                    # left+1 because we are gonna increment it again later
                    while nums[left]==nums[left+1] and right>(left+1):
                        left+=1

                    while nums[right]==nums[right-1] and right>(left+1):
                        right-=1
                    
                    # after checking that it is on the last value of the repeated,
                    # it is now time to move both pointers
                    left+=1
                    right-=1

                elif sum_val>curr_target:
                    right-=1
                else:
                    left+=1
        
        return answer

# time complexity of O(n)
