"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums2_count = {}
        for i in nums2:
            if i not in nums2_count:
                nums2_count[i] = 0
            nums2_count[i] += 1
        for i in nums1:
            if i in nums2_count and nums2_count[i] > 0:
                nums2_count[i] -= 1
                res.append(i)
        return res
