class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        for i in [n//4, n//2, 3*n//4, n]:
            if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) > n//4:
                return arr[i]