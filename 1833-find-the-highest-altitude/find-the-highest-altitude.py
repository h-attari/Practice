class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude, altitude = 0, 0
        for x in gain:
            altitude += x
            highest_altitude = max(highest_altitude, altitude)
        return highest_altitude