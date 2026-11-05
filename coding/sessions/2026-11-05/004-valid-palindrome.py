class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []

        for i in s:
            if (ord(i.lower()) >= ord('a') and ord(i.lower()) <= ord('z')) or (i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                res.append(i.lower())
        
        return True if res == res[::-1] else False
