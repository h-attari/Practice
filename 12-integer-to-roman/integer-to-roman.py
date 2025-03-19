class Solution:
    def intToRoman(self, num: int) -> str:
        i2r = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        ans = []
        for n in i2r.keys():
            while num >= n:
                ans.append(i2r[n])
                num -= n
                
            if num == 0:
                break
                
        return "".join(ans)