class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows-1):
            temp = [1,1]
            last = res[-1]
            index = 0
            while index < len(last)-1 and len(last) > 1:
                num = last[index] + last[index + 1]
                temp.insert(index+1, num)
                index += 1
            res.append(temp)
        return res