class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        '''
        nums.sort()
