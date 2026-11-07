"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
