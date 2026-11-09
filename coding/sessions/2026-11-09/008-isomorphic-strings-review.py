"""
日期：2026-11-09；序号：008
LeetCode 205 Isomorphic Strings / 同构字符串
来源：https://leetcode.com/problems/isomorphic-strings/
难度：简单；时间盒：15 分钟；类型：到期间隔复习

请不要查看旧代码、旧评审或题解。
独立完成完整可运行函数，并说明复杂度；如果卡住，请明确说明卡点。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t, t_to_s = {}, {}

        if len(s) != len(t):return False

        for a, b in zip(s, t):
            if a in s_to_t and s_to_t[a] != b:
                return False 
            if b in t_to_s and t_to_s[b] != a:
                return False 
            s_to_t[a] = b 
            t_to_s[b] = a 
        return True


# 提交口述：时间 O(n)，空间 O(n)。


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

