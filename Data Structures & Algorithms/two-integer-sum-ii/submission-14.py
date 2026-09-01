class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers)-1

        while right > left:
            
            # checking if the target is reached
            sum_val = numbers[right] + numbers[left]

            if sum_val == target:
                return [left+1, right+1]
            
            elif sum_val>target:
                right-=1
            
            else:
                left+=1