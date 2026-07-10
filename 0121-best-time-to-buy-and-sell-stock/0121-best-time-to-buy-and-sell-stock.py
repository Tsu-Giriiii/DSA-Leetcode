class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Brute Force
        '''maxprof = 0
        for i in range(len(prices)-1):
            profit = 0
            for j in range(i,len(prices)):
                profit = prices[j]-prices[i]
                maxprof =max(maxprof,profit)
        return maxprof'''

        maxprof = 0
        i = 0
        for j in range(len(prices)):
            profit = prices[j]-prices[i]
            if profit<0:
                i=j
            else:
                maxprof = max(maxprof,profit)
        return maxprof
