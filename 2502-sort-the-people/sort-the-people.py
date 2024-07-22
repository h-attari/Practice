from functools import cmp_to_key


class Solution:
    def comparator(a, b):
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        else:
            return 0
    
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = [person[0] for person in sorted(zip(names, heights),key=cmp_to_key(Solution.comparator))]
        return result
        