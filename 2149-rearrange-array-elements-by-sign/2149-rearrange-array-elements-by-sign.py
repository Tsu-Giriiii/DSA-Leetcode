class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''#Brute Force
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
        
        return final'''
        res = [0]*len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                res[pos] = num
                pos +=2
            else:
                res[neg]= num
                neg +=2
        return res



