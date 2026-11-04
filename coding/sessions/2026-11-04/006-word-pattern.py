"""
日期：2026-11-04
序号：006
题目：LeetCode 290 - Word Pattern
链接：https://leetcode.com/problems/word-pattern/
难度：Easy
类型：相似题强化
时间盒：25 分钟

请打开链接阅读原题，不查看题解或 LC205 的旧代码。
独立完成；如果卡住，请先写清楚卡在题意、关系设计还是代码实现。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_split = s.split(" ")
        if len(pattern) != len(s_split):return False
        s_to_t, t_to_s = {}, {}

        for a, b in zip(pattern, s_split):
            if a in s_to_t and s_to_t[a] != b:
                return False
            if b in t_to_s and t_to_s[b] != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方
