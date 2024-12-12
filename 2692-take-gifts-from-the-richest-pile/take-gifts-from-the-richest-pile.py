from heapq import heapify, heappush, heappop


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for index in range(len(gifts)):
            gifts[index] = -gifts[index]
        heapify(gifts)
        for _ in range(k):
            temp = -heappop(gifts)
            temp = int(temp ** (0.5))
            heappush(gifts, -temp)
        return -sum(gifts)
        