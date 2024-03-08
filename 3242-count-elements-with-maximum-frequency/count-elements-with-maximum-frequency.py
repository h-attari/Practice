class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        temp_dict = Counter(nums)
        temp_dict = sorted(
            temp_dict.items(), reverse=True,
            key=lambda x: x[1]
        )
        result = check = temp_dict[0][1]
        for ele in temp_dict[1:]:
            if ele[1] == check:
                result += ele[1]
        return result