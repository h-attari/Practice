class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, sum(range(1, n+1))
        
        for num in range(1, n+1):
            left += num
            if left == right:
                return num
            right -= num
        
        return -1