class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        index = 0
        result = []
        while index < len(intervals):
            interval = intervals[index]
            if interval[1] < newInterval[0]:
                result.append(interval)
                index += 1
                continue
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[index:]
            temp = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            print("temp -> ",temp)
            i = index + 1
            while i < len(intervals):
                interval = intervals[i]
                print(interval)
                if interval[0] > temp[1]:
                    result.append(temp)
                    return result + intervals[i:]
                temp[1] = max(temp[1], interval[1])
                i += 1
            result.append(temp)
            break
        return result