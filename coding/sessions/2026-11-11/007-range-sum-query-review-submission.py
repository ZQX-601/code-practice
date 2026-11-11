"""2026-11-11 learner submission transcribed from chat without algorithm changes."""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix = [0]
        for i in range(len(nums)):
            self.prefix.append(self.prefix[i] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]


# 初始化 O(n)，单次查询 O(1)，额外空间 O(n)。
# prefix[i] = sum(nums[0:i])；闭区间查询经 Level 1 单元素反例后修正为
# prefix[right+1] - prefix[left]。
