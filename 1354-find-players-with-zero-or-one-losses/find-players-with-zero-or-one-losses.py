class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won_all = dict()
        lost_all = dict()
        won = list()
        lost = list()
        for match in matches:
            if match[0] not in won_all:
                won_all[match[0]] = 1
            else:
                won_all[match[0]] += 1
            if match[1] not in lost_all:
                lost_all[match[1]] = 1
            else:
                lost_all[match[1]] += 1
        for winner, _ in won_all.items():
            if winner not in lost_all:
                won.append(winner)
        for loser, matches_lost in lost_all.items():
            if matches_lost == 1:
                lost.append(loser)
        return [sorted(won), sorted(lost)]
