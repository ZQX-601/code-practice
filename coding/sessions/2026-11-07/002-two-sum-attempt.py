"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            a, b = nums[i], target - nums[i]
            if b in lookup:
                return [i, lookup[b]]
            lookup[a] = i
        return []
