class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_dict = {}
        index = 0
        while index < len(nums):
            num = nums[index]
            num_count = temp_dict.get(num, 0)
            if num_count == 2:
                nums.pop(index)
                continue
            if num_count == 0:
                temp_dict[num] = 1
            else:
                temp_dict[num] += 1
            index += 1
        return len(nums)