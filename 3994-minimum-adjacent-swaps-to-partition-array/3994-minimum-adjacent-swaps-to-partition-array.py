class Solution(object):
    def minAdjacentSwaps(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD = (10**9)+7
        swapcount = 0
        mid = 0
        high = 0
        for i in nums:
            if i<a:
                swapcount+= high+mid
            elif i<=b:
                swapcount+=high
                mid+=1
            else:
                high+=1
        return swapcount%MOD