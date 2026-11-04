class Solution(object):
    def isAnagram(self, s, t):
        a_lookup = {}
        b_lookup = {}
        for i in s:
            if i not in a_lookup:
                a_lookup[i] = 1
            else:
                a_lookup[i] += 1
        for i in t:
            if i not in b_lookup:
                b_lookup[i] = 1
            else:
                b_lookup[i] += 1
        return True if a_lookup == b_lookup else False
