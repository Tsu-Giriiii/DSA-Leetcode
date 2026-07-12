class Solution(object):
    def minimumCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        prefix = 0
        t = 0
        for i in nums: 
            prefix +=i
            if prefix > k:
                t = max(t,(prefix-1)//k)
        
        return ((t*(t+1))//2)%MOD
                
        