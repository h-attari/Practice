class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        nums_queue = list()
        queue_max_len = k + 1
        for num in nums:
            if not (len(nums_queue) < queue_max_len):
                nums_queue.pop(0)
            if num in nums_queue:
                return True
            nums_queue.append(num)
        return False
