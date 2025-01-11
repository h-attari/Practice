class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # temp_dict = {num:index for index, num in enumerate(nums)}
        temp_dict = {}
        for index, num in enumerate(nums):
            if (target - num) in temp_dict:
                return [temp_dict[(target - num)], index]
            temp_dict[num] = index
        return []
        