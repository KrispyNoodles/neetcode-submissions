class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        curr_set =[]

        def helperFn(i):

            # add it into the answer and return
            if i>=len(nums):
                answer.append(curr_set.copy())
                return
            
            # add it to the curr_set
            curr_set.append(nums[i])
            helperFn(i+1)

            curr_set.pop()
            helperFn(i+1)

        
        helperFn(0)

        return answer