class Solution(object):
    def containsDuplicate(self, nums):
        num_ = []
        for num in nums:
            if num not in num_:
                num_.append(num)
            else:
                return True
        return False
