class Solution(object):
    def containsDuplicate(self, nums):
        loopup = set()
        for num in nums:
            if num in loopup:
                return True
            loopup.add(num)
        return False
