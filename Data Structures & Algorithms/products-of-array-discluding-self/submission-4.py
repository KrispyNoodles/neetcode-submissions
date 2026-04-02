class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []


        # creating two arrays
        # prefix arr
        prefix_arr = []
        prefix_num = 1

        for value in nums:
            prefix_num = prefix_num * value
            prefix_arr.append(prefix_num)
        
        # prefix arr
        postfix_arr = []
        postfix_num = 1

        for value in nums[::-1]:
            postfix_num = postfix_num * value
            postfix_arr.append(postfix_num)

        postfix_arrr = postfix_arr[::-1]

        answer = []

        for index in range(len(nums)):
            # first elemnt
            if index == 0:
                answer.append(postfix_arrr[index+1])

            # last ellement
            elif index == len(nums)-1:
                answer.append(prefix_arr[index-1])

            else:
                value = prefix_arr[index-1] * postfix_arrr[index+1]
                answer.append(value)
        
        return answer
        

