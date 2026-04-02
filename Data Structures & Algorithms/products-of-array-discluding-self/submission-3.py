class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        for index in range(len(nums)):
            temp_arr = nums[:]

            temp_arr.pop(index)

            mul_val = 1
            
            for value in temp_arr:
                mul_val = mul_val * value

            answer.append(mul_val)

        return answer
            
        

