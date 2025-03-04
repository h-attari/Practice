class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        temp_set = set()
        while n > 0:
            temp = 1
            while (temp * 3) <= n:
                temp *= 3
            if temp in temp_set:
                break
            temp_set.add(temp)
            n -= temp
        return True if (n == 0) else False