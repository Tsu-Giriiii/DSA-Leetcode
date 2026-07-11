class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Brute Force
        positive = []
        negative = []
        final = []
        for i in range(len(nums)):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)//2):
            final.append(positive[i])
            final.append(negative[i])
        
        return final

