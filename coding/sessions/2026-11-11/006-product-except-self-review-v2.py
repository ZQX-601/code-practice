"""2026-11-11 learner's second submission; preserves the first auxiliary-array version."""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans
