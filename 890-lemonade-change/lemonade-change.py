class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available_change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 10:
                if available_change[5] == 0:
                    return False
                available_change[5] -= 1
            elif bill == 20:
                if available_change[10] == 0:
                    if available_change[5] < 3:
                        return False
                    available_change[5] -= 3
                else:
                    if available_change[5] == 0:
                        return False
                    available_change[10] -= 1
                    available_change[5] -= 1
            available_change[bill] += 1
        return True
        