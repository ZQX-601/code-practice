"""Learner logic transcribed with normalized formatting and signature."""
def solve(nums,k):
    used = left = ans = 0
    for right,num in enumerate(nums):
        if num == 0:
            used += 1
            while used > k:
                tmp = nums[left]
                if tmp == 0:
                    used -= 1
                left += 1
        ans = max(ans,right-left+1)
    return ans
