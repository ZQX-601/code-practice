"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        lookup = {}
        for word in strs:
            counts = [0] * 26
            for i in word:
                counts[ord(i) - ord('a')] += 1
            key = tuple(counts)
            if key not in lookup:
                lookup[key] = []
            lookup[key].append(word)
        return list(lookup.values())
