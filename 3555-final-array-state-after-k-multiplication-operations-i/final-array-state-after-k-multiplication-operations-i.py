from heapq import heapify, heappush, heappop


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[num, index] for index, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            num_ele = heappop(heap)
            num_ele[0] *= multiplier
            heappush(heap, num_ele)
        for _ in range(len(nums)):
            num, index = heappop(heap)
            nums[index] = num
        return nums
        