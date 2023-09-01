class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            temp = str(bin(num)).replace("0b", "")
            result.append(temp.count("1"))
        return result