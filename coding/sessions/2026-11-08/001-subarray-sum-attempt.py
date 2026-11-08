"""2026-11-08 learner submission; formatting/comments normalized."""
class Solution(object):
    def subarraySum(self, nums, k):
        counts = {0:1}
        res = 0
        total = 0
        for num in nums:
            total += num
            res += counts.get(total - k, 0)
            counts[total] = counts.get(total, 0) + 1
        return res
