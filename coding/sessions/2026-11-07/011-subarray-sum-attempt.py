"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        counts = {0: 1}
        total = 0
        res = 0
        for num in nums:
            total += num
            res += counts.get(total - k, 0)
            counts[total] = counts.get(total, 0) + 1
        return res
