"""2026-11-11 learner submission transcribed from chat without algorithm changes."""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                current = num
                while current + 1 in nums_set:
                    length += 1
                    current += 1
                ans = max(ans, length)
        return ans


# 学习者说明
# 1. num-1 不存在时，num 是一段新连续序列的开端；否则不从 num 重复扩展。
# 2. 初答：for 一直向后，while 不会遍历全部集合。
# 时间 O(n)，空间 O(n)。方法经 Level 1 诊断后从“双指针”修正为哈希结构。
