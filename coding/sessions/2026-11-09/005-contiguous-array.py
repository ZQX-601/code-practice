class Solution(object):
    def findMaxLength(self, nums):
        lookup = {0: -1}
        balance = 0
        longest = 0
        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in lookup:
                longest = max(longest, i - lookup[balance])
            else:
                lookup[balance] = i
        return longest
