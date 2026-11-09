class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0]
        for i in range(len(nums)):
            self.prefix.append(self.prefix[i] + nums[i])

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]
