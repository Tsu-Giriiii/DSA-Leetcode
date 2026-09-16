class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        lo = min(weights)
        hi = sum(weights)
        res = float('inf')

        def check(weights,cap,days):
            left = 0
            sub = 0
            day_count = 0
            for right in range(len(weights)):
                if weights[right]>cap:
                    return False
                sub +=  weights[right]
                if sub > cap:
                    day_count+=1
                    left = right
                    sub = weights[right]
            if sub > 0:
                day_count+=1
            return True if day_count <=days else False

        while lo <= hi:

            mid = lo + (hi-lo)//2
            print(mid,check(weights,mid,days))
            if check(weights,mid,days) and mid < res:
                res = mid
                hi = mid-1
            
            else:
                lo = mid + 1
            
        return res

        
        