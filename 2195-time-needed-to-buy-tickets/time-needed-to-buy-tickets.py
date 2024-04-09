class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] == 0:
            return 0
        
        time = temp =tickets[k]
        tickets[k] = 0
        for index, ticket in enumerate(tickets):
            if ticket < temp:
                time += ticket
            else:
                time += temp
                if index > k:
                    time -= 1
        return time
        