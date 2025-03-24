class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meeting_days = 0
        meetings.sort(key=lambda x: x[0])
        start, end = meetings[0]
        for meeting in meetings:
            if end >= meeting[0]:
                start = min(start, meeting[0])
                end = max(end, meeting[1])
            else:
                meeting_days += (end - start) + 1
                start = meeting[0]
                end = meeting[1]
        meeting_days += (end - start) + 1
        return days - meeting_days