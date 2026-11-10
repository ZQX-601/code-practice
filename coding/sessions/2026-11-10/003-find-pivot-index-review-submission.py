"""2026-11-10 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = 0
        for num in nums:
            total += num
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += nums[i]
        return -1
