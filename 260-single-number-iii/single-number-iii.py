class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp_num = 0
        for num in nums:
            temp_num ^= num
        
        index = 0
        while index < 32:
            if (temp_num & (1 << index)) != 0:
                break
            index += 1
        
        lst1, lst2 = [], []
        for num in nums:
            if (num & (1 << index)) == 0:
                lst1.append(num)
            else:
                lst2.append(num)
        
        a, b = 0, 0
        for num in lst1:
            a ^= num
        for num in lst2:
            b ^= num
        
        return [a, b]
        