class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        for left in range(n-1):
            sums = nums[left]
            for right in range(left+1, n):
                sums += nums[right]
                if sums % k == 0:
                    return True
        return False
