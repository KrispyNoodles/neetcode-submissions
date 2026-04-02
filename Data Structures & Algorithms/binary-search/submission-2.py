from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # it is already sorted in ascending

        left = 0
        right = len(nums)

        while right > left:

            # // means round to nearest int
            # add the previous left 
            middle = left + ((right-left)//2)

            # if the middle value is bigger than the target means gotta search left side (the middle value OVERSHOT LERH)
            if nums[middle] > target:
                print('found value in this section')
                # shift the right boundary to the middle
                right = middle

            # if the middle value is smaller than the target (the middle UNDERSHOT-ed) search ride side
            else:
                print('found value in this section instead')
                
                # move the left marker to the right of the middle
                left = 1 + middle
           
        # they will convert to the same number
        # increment left
        # it returns the upper bound of the value
        # so when you give a super huge number that is out of the array it will give you an index closest to it

        # but if there is a value like 8 in [-1,0,3,5,9,12,19] it will give 9 instead
        # or for 9 in [-1,0,3,5,9,12,19] it will give 12 instead, the largest on the right

        # therefore a -1 is needed to check if it is the value
        if nums[left-1]==target:
            return left-1

        else:
            return -1