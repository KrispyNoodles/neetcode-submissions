class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        index_1 = 0
        index_2 = 0

        for index in range(len(nums)):

            # initating
            index_1 = index

            # finidng the other target
            target_2 = target-nums[index_1]

            if target_2 in nums:
                # find the index of target 2
                index_2 = nums.index(target_2)

                # checking if the index is index_1 
                if index_2 != index_1:

                    # returning it as an array
                    return sorted([index_1, index_2])

                