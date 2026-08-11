class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        mp=0
        for x in prices:
            if x<min:
                min=x
            p=x-min
            if p>mp:
                mp=p
        return mp
        
        