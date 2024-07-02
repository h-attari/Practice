class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for ele in nums1:
            if len(nums2) > 0 and ele in nums2:
                result.append(ele)
                nums2.remove(ele)
        return result