"""Transcribed learner logic with normalized names and formatting."""

def min_window(target, nums):
    ans = len(nums) + 1
    total = left = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1
    return ans if ans != len(nums) + 1 else 0

def min_binary(target, nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    ans = len(nums) + 1
    for left in range(len(nums)):
        need = prefix[left] + target
        lo, hi = left + 1, len(prefix)
        while lo < hi:
            mid = (lo + hi) // 2
            if prefix[mid] < need:
                lo = mid + 1
            else:
                hi = mid
        if lo < len(prefix):
            ans = min(ans, lo - left)
    return ans if ans != len(nums) + 1 else 0

def check_subarray_sum(nums, k):
    lookup = {0: -1}
    total = 0
    for i, num in enumerate(nums):
        total += num
        remainder = total % k
        if remainder in lookup:
            if i - lookup[remainder] >= 2:
                return True
        else:
            lookup[remainder] = i
    return False

def count_product_less(nums, k):
    if k <= 1:
        return 0
    ans = left = 0
    product = 1
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        ans += right - left + 1
    return ans

def count_sum_less(nums, k):
    sums = left = ans = 0
    for right, num in enumerate(nums):
        sums += num
        while sums >= k:
            sums -= nums[left]
            left += 1
        ans += right - left + 1
    return ans

def count_sum_at_least(nums, k):
    sums = left = ans = 0
    for num in nums:
        sums += num
        while sums >= k:
            sums -= nums[left]
            left += 1
        ans += left
    return ans
