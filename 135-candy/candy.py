class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        i, j = 1, len(ratings)-2
        while i < len(ratings) and j > -1:
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i]  = candies[i-1] + 1
                result = candies[i]
            if ratings[j] > ratings[j+1] and candies[j] <= candies[j+1]:
                candies[j]  = candies[j+1] + 1
            i += 1
            j -= 1
        
        print(candies)
        return sum(candies)
        