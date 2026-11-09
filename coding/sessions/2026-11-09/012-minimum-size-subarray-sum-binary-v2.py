"""
日期：2026-11-09；序号：012-v2
LeetCode 209 Minimum Size Subarray Sum / 长度最小的子数组
来源：https://leetcode.com/problems/minimum-size-subarray-sum/
难度：中等；类型：前缀和 + 二分修正版

说明：保留 012 中首次提交的边界错误，本文件记录学习者修正后的原始答案。
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 双指针
        # ans = MAX_VALUE = 1000000
        # total = 0
        # left = 0
        # for right in range(len(nums)):
        #     total += nums[right]
        #     while total >= target:
        #         ans = min(ans, right - left + 1)
        #         total -= nums[left]
        #         left += 1

        # return ans if ans != MAX_VALUE else 0

        # 二分 + 前缀和

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        ans = len(nums) + 1
        for left in range(len(nums)):
            need = prefix[left] + target
            right = self.bisect_search(prefix, need, left + 1)
            if right < len(prefix):
                ans = min(ans, right - left)
        return ans if ans != len(nums) + 1 else 0

    def bisect_search(self, nums, target, idx=0):
        left, right = idx, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
