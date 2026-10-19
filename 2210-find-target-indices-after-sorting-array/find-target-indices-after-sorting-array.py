class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    index = mid
                    while index < len(nums) and nums[index] == target:
                        result.append(index)
                        index += 1
                    break
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result
