class Solution(object):
    def trailingZeroes(self, n):
        f=1
        for i in range(1,n+1):
            f=f*i
        if f%10==0:
            return 1
        else:
            return 0

        