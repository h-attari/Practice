class Solution:
    def check(self, old, new, target):
        return target <= (new - old - 1)
    
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_1 = -1
        for index, num in enumerate(nums):
            if num != 1:
                continue
            if last_1 != -1:
                if self.check(last_1, index, k) is False:
                    return False
            last_1 = index
        return True