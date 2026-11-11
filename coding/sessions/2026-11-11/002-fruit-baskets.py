"""Learner logic transcribed with normalized formatting and signature."""
def solve(fruits):
    ans = 0
    left = 0
    counts = {}
    for right in range(len(fruits)):
        counts[fruits[right]] = counts.get(fruits[right],0)+1
        while len(counts)>2:
            tmp = fruits[left]
            counts[tmp] -= 1
            if counts[tmp] == 0:
                del counts[tmp]
            left += 1
        ans = max(ans,right-left+1)
    return ans
