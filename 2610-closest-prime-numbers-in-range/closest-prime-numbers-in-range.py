class Solution:
    def get_primes(self, start, end):
        lst = [True] * (end + 1)
        lst[0] = lst[1] = False
        for num in range(2, (int(end ** 0.5) + 1)):
            if lst[num] is True:
                for j in range((num * num), end + 1, num):
                    lst[j] = False
        primes = [index for index in range(start, end+1) if lst[index] is True]
        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.get_primes(left, right)
        result = [-1, -1]
        temp_diff = float("inf")
        index1, index2 = 0, 1
        while index2 < len(primes):
            if (primes[index2] - primes[index1]) < temp_diff:
                temp_diff = primes[index2] - primes[index1]
                result[0], result[1] = primes[index1], primes[index2]
            index1 += 1
            index2 += 1
        return result