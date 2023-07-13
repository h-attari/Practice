class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_sort_list = [0] * 3
        for num in nums:
            count_sort_list[num] += 1
        nums_index = 0
        for count_index in range(len(count_sort_list)):
            for _ in range(count_sort_list[count_index]):
                nums[nums_index] = count_index
                nums_index += 1
