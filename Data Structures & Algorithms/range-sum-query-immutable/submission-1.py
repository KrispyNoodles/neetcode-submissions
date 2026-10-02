class NumArray:

    def __init__(self, nums: List[int]):

        self.arr = nums
        

    def sumRange(self, left: int, right: int) -> int:

        # retrieve that array and do the sum
        calc = self.arr[left:right+1]
        print(calc)
        return sum(calc)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)