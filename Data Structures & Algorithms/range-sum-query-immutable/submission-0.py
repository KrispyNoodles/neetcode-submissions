class NumArray:

    def __init__(self, nums: List[int]):
        
        # creating a prefix
        self.prefix = []

        total = 0

        for i in nums:
            total+=i
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:

        # returning the answer
        left_val = self.prefix[left-1] if left>0 else 0
        right_val = self.prefix[right]
        
        return right_val-left_val


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)