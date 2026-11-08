"""2026-11-08 learner submission; formatting/comments normalized."""
class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        total = 0
        left_sum = 0
        for i in range(n):
            total += nums[i]
        for i in range(n):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
