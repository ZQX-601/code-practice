"""
日期：2026-11-09；序号：012
LeetCode 209 Minimum Size Subarray Sum / 长度最小的子数组
来源：https://leetcode.com/problems/minimum-size-subarray-sum/
难度：中等；时间盒：30 分钟；类型：同题第二种解法教学

目标：使用前缀和与二分查找完成 O(n log n) 解法。
不要查看现成代码。先完成下方推导，再写二分；如果卡住，请指出是前缀定义、不等式还是二分边界。
"""

# 1. 前缀和定义
# 写出 prefix[i] 表示什么，并手算 nums=[2,3,1,2,4,3] 时的 prefix。


# 2. 子数组和公式
# 用 prefix 表示 nums[left:right] 的和（right 为开区间）。


# 3. 二分目标与不变量
# 固定 left 后，需要找到怎样的最小 right？把条件写成关于 prefix[right] 的不等式。


# 4. 时间/空间复杂度


# 5. 最终代码
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
            right = self.bisect_search(prefix, need, left+1)
            if right < len(nums):
                ans = min(ans, right - left)
        return ans if ans != len(nums) + 1 else 0



    def bisect_search(self, nums, target, idx = 0):
        left, right = idx, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        return left


# 6. 自测用例与 dry run


# 7. 用时、使用过的提示等级、仍不确定的地方

