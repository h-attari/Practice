class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = str(num)
        result = ""
        index = 0
        for digit in temp:
            if int(digit) == 6:
                result += f"9{temp[index+1:]}"
                break
            result += digit
            index += 1
        return int(result)