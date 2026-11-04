"""
日期：2026-11-04
序号：004
题目：LeetCode 383 - Ransom Note
链接：https://leetcode.com/problems/ransom-note/
难度：Easy
类型：新题
时间盒：20 分钟

请打开链接阅读原题，不查看题解或历史答案。
先独立完成；如果卡住，直接告诉教练你卡在题意、思路还是代码。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_lookup = {}
        for item in magazine:
            if item not in m_lookup:
                m_lookup[item] = 1
            else:
                m_lookup[item] += 1
        for item in ransomNote:
            if item not in m_lookup:
                return False
            elif m_lookup[item] == 0:
                return False
            m_lookup[item] -= 1

        return True


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方
