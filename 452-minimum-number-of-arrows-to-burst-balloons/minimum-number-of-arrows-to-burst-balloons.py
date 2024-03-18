class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # print(points)
        points = sorted(points, key=lambda x: x[1])
        # print(points)
        lst = []
        start_index = 0
        while start_index < len(points):
            temp = [points[start_index][0],points[start_index][1]]
            temp_index = start_index
            for end_index in range(start_index+1,len(points)):
                if points[end_index][0] <= points[start_index][1]:
                    temp[1] = points[end_index][1]
                    temp_index = end_index
                else:
                    break
            start_index = temp_index + 1
            lst.append(temp)
        # print(lst)
        return len(lst)