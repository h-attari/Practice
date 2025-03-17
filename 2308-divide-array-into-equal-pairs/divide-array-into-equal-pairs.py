class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
        for num, count in temp_dict.items():
            if count & 1 == 1:
                return False
        return True
        