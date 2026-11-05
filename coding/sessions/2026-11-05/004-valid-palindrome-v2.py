class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # res = []

        # for i in s:
        #     if i.isalnum():
        #         res.append(i.lower())
        
        # return True if res == res[::-1] else False
        left, right = 0, len(s)
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right-1].isalnum():
                right -= 1
            elif s[left].lower() != s[right-1].lower():
                return False 
            else:
                left += 1
                right -= 1
        return True
