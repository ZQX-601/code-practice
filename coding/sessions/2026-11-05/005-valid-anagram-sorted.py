"""
会话日期：2026-11-05
序号：005（从误聊项目中的原序号 003 迁移）
题目：LeetCode 242 - Valid Anagram
来源：https://leetcode.com/problems/valid-anagram/
难度：Easy
类型：复测
时限：25 分钟
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):return False
        for a, b in zip(sorted(s), sorted(t)):
            if a != b:
                return False 
        return True
