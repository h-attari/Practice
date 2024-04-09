class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] != 0:
            for index in range(len(tickets)):
                if tickets[index] > 0:
                    tickets[index] -= 1
                    time += 1
                if index == k and tickets[index] == 0:
                    break
        return time
        