"""
日期：2026-11-09；序号：007
LeetCode 125 Valid Palindrome / 验证回文串
来源：https://leetcode.com/problems/valid-palindrome/
难度：简单；时间盒：15 分钟；类型：到期间隔复习

请不要查看 2026-11-05 的代码、评审或题解。
独立完成完整可运行函数；如果记不清优化方式，可以先写任何正确方案。
"""

# 1. 题意复述与需要澄清的问题


# 2. 暴力解法


# 3. 优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # res = []

        # for i in s:
        #     if i.isalnum():
        #         res.append(i.lower())
        
        # return True if res == res[::-1] else False
        
        left, right = 0, len(s)
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right-1].isalnum():
                right -= 1
            elif s[left].lower() != s[right-1].lower():
                return False 
            else:
                left += 1
                right -= 1
            
        return True


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

