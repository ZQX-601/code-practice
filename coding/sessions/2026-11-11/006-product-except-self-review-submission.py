"""2026-11-11 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        left_product = [1] * n
        right_product = [1] * n

        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = left_product[i] * right_product[i]

        return ans


# 推导记录
# 方法经 Level 1 诊断后从“双指针”修正为前缀/后缀累计。
# 暴力时间 O(n^2)；本实现候选时间 O(n)，辅助数组空间 O(n)。
