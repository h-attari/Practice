class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        if len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))
        elif len(version1) > len(version2):
            version2 += [0] * (len(version1) - len(version2))
        
        for v1, v2 in zip(version1, version2):
            v1, v2 = int(v1), int(v2)
            if v1 < v2:
                return -1
            if v2 < v1:
                return 1
        
        return 0
        