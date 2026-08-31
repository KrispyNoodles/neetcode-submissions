class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        
        while right>left:

            sum_val = numbers[left] + numbers[right]

            if sum_val == target:
                return [left+1, right+1]

            # move right to the left by 1
            elif sum_val > target:
                right-=1
            else:
                left+=1

