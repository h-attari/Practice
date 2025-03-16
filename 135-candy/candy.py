class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index-1] and result[index] <= result[index-1]:
                result[index]  = result[index-1] + 1
        for index in range(len(ratings)-2, -1, -1):
            if ratings[index] > ratings[index+1] and result[index] <= result[index+1]:
                result[index]  = result[index+1] + 1
        # print(result)
        return sum(result)
        