class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        ap_diff = arr[1] - arr[0]
        for index in range(1, len(arr)-1):
            temp_diff = arr[index+1] - arr[index]
            if temp_diff != ap_diff:
                return False
        return True