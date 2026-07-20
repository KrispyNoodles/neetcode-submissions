class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # if len of nums less than 3 means no possible combi
        if len(nums)<3:
            return []
        
        # sort the nums first
        nums.sort()

        answer = []

        # let each of the number be the index to find
        # from 0 to the 2nd last
        for i, value in enumerate(nums):

            # to check that it is not the first value of the array
            # and it is the same as the previous
            if i>0 and value == nums[i-1]:
                continue
            
            find_value = -nums[i]

            left, right = i+1, len(nums)-1

            while right>left:
                
                total_sum = nums[left]+nums[right]

                # add it into the answer
                if find_value == total_sum:
                    answer.append([nums[i], nums[left], nums[right]])
                    left+=1

                    # checking if the next nums is the same
                    while nums[left]==nums[left-1] and right>left:
                        left+=1                    
                
                # if it is bigger move the right to the left index
                elif total_sum > find_value:
                    right-=1
                else:
                    left+=1
        
        return answer
            

            
