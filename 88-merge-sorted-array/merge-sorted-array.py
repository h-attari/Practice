class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m
        for num in nums2:
            nums1[index] = num
            index += 1
        nums1.sort()