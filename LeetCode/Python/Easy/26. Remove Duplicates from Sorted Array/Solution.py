class Solution(object):
    def removeDuplicates(self, nums):
        w=0
        for r in range(1,len(nums)):
            if nums[r]!=nums[w]:
                w=w+1
                nums[w]=nums[r]
        return w+1