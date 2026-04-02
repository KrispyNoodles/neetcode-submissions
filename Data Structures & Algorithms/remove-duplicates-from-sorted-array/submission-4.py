from typing import List

# trying to optimise
# cant return a set as it has to remove from the list
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        
        # set retrieves all the unique and sorted converts it back to a set
        sorted_list = sorted(set(nums))

        print(sorted_list)

        # adjust the current length of the list to be the same as the sorted_list
        nums[:len(sorted_list)] = sorted_list

        return len(sorted_list)

        