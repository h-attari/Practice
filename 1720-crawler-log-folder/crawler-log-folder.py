class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dir_depths = 0
        for dir_name in logs:
            if dir_name == "./":
                continue
            if dir_name == "../":
                if dir_depths > 0:
                    dir_depths -= 1
                continue
            dir_depths += 1
        return dir_depths
        