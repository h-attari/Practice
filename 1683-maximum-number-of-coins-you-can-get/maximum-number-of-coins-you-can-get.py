class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        s,x=0,0
        y=len(piles)-2
        while(x<y):
            s+=piles[y]
            x+=1
            y-=2
        return s