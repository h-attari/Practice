class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if not (((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
            return "none"
        types = ["equilateral", "isosceles", "scalene"]
        return types[len(set(nums))-1]
        