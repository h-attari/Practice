class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = max(arr)
        for index in range(len(arr)-1):
            if arr[index] >= max_num:
                max_num = max(arr[index+1:])
            arr[index] = max_num
        arr[-1] = -1
        return arr