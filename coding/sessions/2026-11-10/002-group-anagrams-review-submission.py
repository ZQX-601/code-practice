"""2026-11-10 learner submission transcribed from chat; HTML/Markdown escapes normalized."""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lookup = {}
        for str_ in strs:
            tmp = "".join(sorted(str_))
            if tmp not in lookup:
                lookup[tmp] = []
            lookup[tmp].append(str_)

        return list(lookup.values())


# 学习者复杂度：O(n*k) 时间，O(n*k) 空间。
