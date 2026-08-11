class Solution(object):
    def removeElement(self, nums, val):
        w=0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[w]=nums[r]
                w=w+1
        return w
        