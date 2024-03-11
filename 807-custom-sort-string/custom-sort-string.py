class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp_dict = {char:index for index,char in enumerate(order)}
        for char in s:
            if char in temp_dict:
                continue
            temp_dict[char] = float("inf")
        result =  sorted(
            s,
            key=cmp_to_key(
                lambda x,y: 1 if temp_dict[x] > temp_dict[y] else -1
            )
        )
        return "".join(result)
        