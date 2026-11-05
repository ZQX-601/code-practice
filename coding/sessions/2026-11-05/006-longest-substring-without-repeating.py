"""
日期：2026-11-05；序号：006
LeetCode 3 Longest Substring Without Repeating Characters
来源：https://leetcode.com/problems/longest-substring-without-repeating-characters/
难度：中等；时间盒：35 分钟；类型：新题

请独立阅读题目与约束，不要查看旧代码、题解或提示。
先写一个保证正确的直接方案，再思考如何减少重复工作。
如果没有完成优化，也请保留已经确认正确的思路和代码。
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

        lookup = defaultdict(int)
        start = 0
        ans = 0
        for end in range(len(s)):
            tmp = s[end]
            lookup[tmp] += 1
            while lookup[tmp] > 1:
                tmp2 = s[start]
                lookup[tmp2] -= 1
                start += 1
            ans = max(ans, end-start+1)
        return ans


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

