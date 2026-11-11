"""Learner logic transcribed with normalized formatting and signature."""
def solve(nums,k):
    if k <= 1:return 0
    product = 1
    left = 0
    ans = 0
    for right,num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        ans += right-left+1
    return ans
