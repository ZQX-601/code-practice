"""
日期：2026-11-09；序号：010
LeetCode 3 Longest Substring Without Repeating Characters
来源：https://leetcode.com/problems/longest-substring-without-repeating-characters/
难度：中等；时间盒：25 分钟；类型：到期间隔复习

请不要查看旧代码、旧评审或题解。
独立完成完整可运行函数，并说明核心不变量及最坏时间、空间复杂度。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        start = 0
        res = 0
        for end in range(len(s)):
            tmp = s[end]
            lookup[tmp] = lookup.get(tmp, 0) + 1
            while lookup[tmp] > 1:
                tmp2 = s[start]
                lookup[tmp2] -= 1
                start += 1
            res = max(res, end-start + 1)
        return res


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

