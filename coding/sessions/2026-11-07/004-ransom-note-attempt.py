"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        m_lookup = {}
        for i in magazine:
            if i not in m_lookup:
                m_lookup[i] = 0
            m_lookup[i] += 1
        for i in ransomNote:
            if i not in m_lookup:
                return False
            elif m_lookup[i] == 0:
                return False
            else:
                m_lookup[i] -= 1
        return True
