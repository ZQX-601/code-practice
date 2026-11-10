"""2026-11-10 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {0: -1}
        total = 0
        ans = 0
        [0, 1, 1, 1, 1, 1, 0, 0, 0]
        [-1, 0, 1, 2, 3, 4, 3, 2, 1]
        for i in range(len(nums)):
            total += 1 if nums[i] == 1 else -1
            if total in lookup:
                ans = max(ans, i - lookup[total])
            else:
                lookup[total] = i

        return ans


# 学习者声明：参考了之前的提交记录才完成。
