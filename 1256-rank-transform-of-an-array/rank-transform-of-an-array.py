class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp_dict = {value:(index+1) for index,value in enumerate(sorted(list(set(arr))))}
        result = [None] * len(arr)
        for index in range(len(arr)):
            result[index] = temp_dict.get(arr[index])
        return result