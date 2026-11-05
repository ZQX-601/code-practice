from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lookup = defaultdict(int)
        start = 0
        ans = 0
        for end in range(len(s)):
            tmp = s[end]
            lookup[tmp] += 1
            while lookup[tmp] > 1:
                tmp2 = s[start]
                lookup[tmp2] -= 1
                start += 1
            ans = max(ans, end-start+1)
        return ans
