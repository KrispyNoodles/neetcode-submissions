class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating a set
        set_ans = set(nums)

        for index, value in enumerate(nums):
            if (target-value) in nums:

                # finding the index
                for index_2, value_2 in enumerate(nums):
                    if value_2 == target-value and index!=index_2:
                        return [index, index_2]

                