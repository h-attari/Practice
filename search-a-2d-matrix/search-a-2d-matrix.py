def find_row(matrix: List[List[int]], target: int) -> int:
    first, last = 0, len(matrix)-1
    while first <= last:
        mid = (first + last) // 2
        if matrix[mid][0] <= target:
            if matrix[mid][-1] >= target:
                return mid
            first = mid + 1
            continue
        last = mid - 1
    return 0


def find_num(lst: List[int], target: int) -> bool:
    first, last = 0, len(lst)-1
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = find_row(matrix, target)
        return find_num(matrix[row], target)
        