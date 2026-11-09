"""
日期：2026-11-09；序号：011
LeetCode 209 Minimum Size Subarray Sum / 长度最小的子数组
来源：https://leetcode.com/problems/minimum-size-subarray-sum/
难度：中等；时间盒：25 分钟；类型：继续未完成题目（第一种实现）

题目中的数组元素为正整数。此前已介绍区间扩张和收缩条件，本次需要独立写成完整代码。
不要查看现成代码或题解；本文件只完成第一种线性实现，第二种前缀和加二分随后单独练习。
"""

# 1. 题意复述与需要澄清的问题


# 2. 直接解法


# 3. 线性优化思路与核心不变量


# 4. 时间/空间复杂度


# 5. 最终代码
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = MAX_VALUE = 1000000
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return ans if ans != MAX_VALUE else 0


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

