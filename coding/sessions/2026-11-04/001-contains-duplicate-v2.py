class Solution(object):
    def containsDuplicate(self, nums):
        num_ = set()
        for num in nums:
            if num not in num_:
                num_.add(num)
            else:
                return True
        return False
