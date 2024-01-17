class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp_set = set(arr)
        occ_list = list()
        for ele in temp_set:
            temp = arr.count(ele)
            if temp in occ_list:
                return False
            occ_list.append(temp)
        return True