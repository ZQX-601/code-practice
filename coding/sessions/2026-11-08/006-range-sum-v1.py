class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, left, right):
        sums = 0
        for i in range(left, right+1):
            sums += self.nums[i]
        return sums
