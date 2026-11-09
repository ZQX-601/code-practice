class Solution(object):
    def checkSubarraySum(self, nums, k):
        total = 0
        lookup = {0:-1}
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder in lookup:
                if i - lookup[remainder] >= 2:
                    return True
            else:
                lookup[remainder] = i
        return False
