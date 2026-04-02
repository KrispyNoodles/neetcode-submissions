class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # creating two arrays
        nums_1 = []
        value_cal = 1

        for value in nums:
            value_cal = value_cal*value
            nums_1.append(value_cal)

        # then create a reverse
        nums_2 = []
        nums = nums[::-1]
        value_cal = 1

        for value in nums:
            value_cal = value_cal*value
            nums_2.append(value_cal)
        
        # flip the nums_2 arr
        nums_2 = nums_2[::-1]

        # create a final answer array
        ans_arr = []
        

        # append the second element of nums_2
        ans_arr.append(nums_2[1])

        # run from index 1 to the second last element
        for index in range(1,len(nums)-1):          

            answer_val = nums_1[index-1] * nums_2[index+1]
            ans_arr.append(answer_val)
        
        # append the second last elelemtn of nums_1
        ans_arr.append(nums_1[-2])

        return ans_arr

# time complecity of O(n) becuase of for loop
# space complexity of O(n)
