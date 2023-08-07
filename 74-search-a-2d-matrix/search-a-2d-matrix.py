class Solution:
    def find_row(self, matrix: List[List[int]], target: int) -> int:
        first, last = 0, len(matrix)-1
        while first <= last:
            mid = (first + last) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            if target < matrix[mid][0]:
                last = mid - 1
            else:
                first = mid + 1
        return -1
    
    def find_num(self, num_list: List[int], num: int) -> bool:
        first, last = 0, len(num_list)-1
        while first <= last:
            mid = (first + last) // 2
            if num_list[mid] == num:
                return True
            if num_list[mid] < num:
                first = mid + 1
            else:
                last = mid - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_row = self.find_row(matrix, target)
        return False if matrix_row == -1 else self.find_num(matrix[matrix_row], target)
        