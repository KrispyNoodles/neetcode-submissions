class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for all values store in the dict
        new_dict = {}

        for index, val in enumerate(nums):
            
            # checking if the answer exist
            if (target-val) in new_dict.keys():
                return [new_dict[target-val], index]

            # if the answer not inside, continue adding
            new_dict[val] = index
        

