class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = None
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
            if temp_dict[num] > (len(nums) // 2):
                result = num
                break
        return result
        