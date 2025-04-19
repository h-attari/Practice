class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]

        for cur_start, cur_end in intervals[1:]:
            if end >= cur_start:
                end = max(end, cur_end)
            else:
                result.append([start, end])
                start = cur_start
                end = cur_end
        result.append([start, end])
    
        return result
        