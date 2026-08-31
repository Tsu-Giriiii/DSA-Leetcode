class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<(m*k):
            return -1
        lo = 1
        hi = max(bloomDay)
        res = hi
        while lo <=hi:
            
            mid = lo + (hi-lo)//2

            if self.check(mid,bloomDay,m,k):
                res =mid
                hi = mid -1
            else:
                lo = mid + 1
        return res
    
    def check(self,mid,bloomDay,m,k):
        # check if m distict groups of k values in bloomDay are less than mid
        
        count_groups = 0
        count_vals = 0
        for day in bloomDay:
            if day<=mid:
                count_vals+=1
                if count_vals==k:
                    count_groups+=1
                    count_vals = 0
                    if count_groups==m:
                        return True
        
            else:
                count_vals = 0
        
        return False
