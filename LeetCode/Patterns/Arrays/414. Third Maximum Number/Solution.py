class Solution(object):
    def thirdMax(self, nums):
        
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')

        for x in nums:
            if first==x or second==x or third==x:
                continue
            
            if x>first:
                third=second
                second=first
                first=x

            elif x>second:
                third=second
                second=x
            
            elif x>third:
                third=x

        if third==float('-inf'):
            return first

        return third
        