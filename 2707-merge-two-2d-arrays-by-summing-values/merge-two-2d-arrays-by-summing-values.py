class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            num1 = nums1[i]
            num2 = nums2[j]
            if num1[0] == num2[0]:
                result.append([num1[0], (num1[1] + num2[1])])
                i += 1
                j += 1
            elif num1[0] < num2[0]:
                result.append(num1)
                i += 1
            else:
                result.append(num2)
                j += 1
        if i < len(nums1):
            result += nums1[i:]
        elif j < len(nums2):
            result += nums2[j:]
        return result