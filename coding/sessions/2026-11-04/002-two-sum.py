class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            a, b = nums[i], target - nums[i]
            if b in lookup:
                return [i, lookup[b]]
            lookup[a] = i
        return []
