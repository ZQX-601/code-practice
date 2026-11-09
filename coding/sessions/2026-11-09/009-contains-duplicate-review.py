"""
日期：2026-11-09；序号：009
LeetCode 217 Contains Duplicate / 存在重复元素
来源：https://leetcode.com/problems/contains-duplicate/
难度：简单；时间盒：10 分钟；类型：到期间隔复习

请不要查看旧代码、旧评审或题解。
独立完成完整可运行函数，并准确说明最坏时间、空间复杂度。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = set()

        for num in nums:
            if num not in lookup:
                lookup.add(num)
            else:
                return True
        return False


# 提交口述：时间 O(n)，空间最坏 O(n)。


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

