"""Learner logic transcribed with normalized formatting and signature."""
def solve(s,k):
    lookup = {}
    ans = left = 0
    for right,str_ in enumerate(s):
        lookup[str_] = lookup.get(str_,0)+1
        while right-left+1-max(lookup.values()) > k:
            lookup[s[left]] -= 1
            left += 1
        ans = max(ans,right-left+1)
    return ans
