"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def wordPattern(self, pattern, s):
        a_to_b, b_to_a = {}, {}
        s_split = s.split(" ")
        if len(pattern) != len(s_split):
            return False
        for a, b in zip(pattern, s_split):
            if a in a_to_b and a_to_b[a] != b:
                return False
            if b in b_to_a and b_to_a[b] != a:
                return False
            a_to_b[a] = b
            b_to_a[b] = a
        return True
