class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp_set = set()
        for num in arr:
            if num*2 in temp_set or num/2 in temp_set:
                return True
            temp_set.add(num)
        return False