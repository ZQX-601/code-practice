"""2026-11-10 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {0: 1}
        sums = 0
        res = 0
        for i in range(len(nums)):
            sums += nums[i]

            res += counts.get(sums - k, 0)

            counts[sums] = counts.get(sums, 0) + 1

        return res


# 学习者声明：没有形成独立回忆，查看之前的题解后完成。
# 学习者诊断：做完后再次遇到仍不会，尚未掌握前缀和计数的精髓。
