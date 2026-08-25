class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp_set = set(nums)
        num = k
        while True:
            if num in temp_set:
                num += k
                continue
            break
        return num
        