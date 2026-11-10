"""2026-11-10 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lookup = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            lookup[s[right]] = lookup.get(s[right], 0) + 1
            while lookup[s[right]] > 1:
                lookup[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 学习者说明
# 时间 O(n)，空间最差 O(n)。
# 固定 right，滑动窗口找无重复子串。
# 因为 right 移动，while 不会再把 s 遍历一遍。
# 自测："sdsad"、"bbbabc"。
