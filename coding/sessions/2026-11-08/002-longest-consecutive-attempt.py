"""2026-11-08 learner submission; formatting/comments normalized."""
class Solution(object):
    def longestConsecutive(self, nums):
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                tmp = 1
                current = num
                while current + 1 in nums_set:
                    tmp += 1
                    current += 1
                ans = max(ans, tmp)
        return ans
