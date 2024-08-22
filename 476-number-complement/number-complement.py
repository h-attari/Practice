class Solution:
    def findComplement(self, num: int) -> int:
        switch = False
        for index in range(31, -1, -1):
            if switch is False:
                if ((1 << index) & num) == 0:
                    continue
                switch = True
            num = (1 << index) ^ num
        return num
        