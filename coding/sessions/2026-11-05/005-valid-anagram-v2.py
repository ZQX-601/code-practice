"""
会话日期：2026-11-05
序号：005 v2（从误聊项目中的原序号 004 迁移）
题目：LeetCode 242 - Valid Anagram（线性时间改写）
来源：https://leetcode.com/problems/valid-anagram/
难度：Easy
类型：优化尝试
时限：15 分钟

已独立识别的目标：不依赖排序位置，比较每种字符的出现数量。
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a_lookup = {}
        b_lookup = {}
        for i in s:
            if i not in a_lookup:
                a_lookup[i] = 1
            else:
                a_lookup[i] += 1

        for i in t:
            if i not in b_lookup:
                b_lookup[i] = 1
            else:
                b_lookup[i] += 1
        
        return True if a_lookup == b_lookup else False


# 时间 O(n)，空间 O(n)。
# 提示声明：Level 1 诊断问题，未提供数据结构或伪代码。
