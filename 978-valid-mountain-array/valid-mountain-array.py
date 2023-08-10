class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        slope = 0
        for index in range(1, len(arr)):
            if arr[index] == arr[index-1]:
                return False
            if arr[index] < arr[index-1]:
                if slope == 0:
                    return False
                slope = -1
            else:
                if slope == -1:
                    return False
                slope = 1
            index += 1
        return True if slope == -1 else False