class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        temp_dict, subarray_sum = {0:-1}, 0
        for index, num in enumerate(nums):
            if k != 0:
                subarray_sum = (subarray_sum + num) % k
            else:
                subarray_sum += num
            if subarray_sum not in temp_dict:
                temp_dict[subarray_sum] = index
            else:
                if index - temp_dict[subarray_sum] >= 2:
                    return True
        return False