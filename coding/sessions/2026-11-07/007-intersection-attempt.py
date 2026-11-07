"""2026-11-07 submission archive; executable logic transcribed from chat.
Comments/formatting normalized. See adjacent review for evidence and changes.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set, nums2_set = set(nums1), set(nums2)
        res = []
        if len(nums1_set) > len(nums2_set):
            nums1_set, nums2_set = nums2_set, nums1_set
        for i in nums2_set:
            if i in nums1_set:
                res.append(i)
        return res
