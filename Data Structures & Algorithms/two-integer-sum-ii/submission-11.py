class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1

        while right>left:

            sum_val = numbers[left] + numbers[right] 
         
            # checking if target is reached
            if sum_val==target:
                # 1-index
                return [left+1, right+1]
            
            # if more means the right value is useless
            elif sum_val>target:
                right-=1
            
            else:
                # this means that the small value is useless
                left+=1

# time complexity of O(n)
# space complexity of O(1) 