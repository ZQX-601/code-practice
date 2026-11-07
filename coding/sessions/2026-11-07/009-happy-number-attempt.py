"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def isHappy(self, n):
        lookup = set()
        while True:
            n = sum(int(i) * int(i) for i in str(n))
            if n > 2**31 - 1:
                return False
            if n == 1:
                return True
            if n in lookup:
                return False
            lookup.add(n)
