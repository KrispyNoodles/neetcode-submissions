class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # build counter and check if each value can divide by 2
        m = Counter(nums)

        for value in m.values():
            if value%2!=0:
                return False
        return True