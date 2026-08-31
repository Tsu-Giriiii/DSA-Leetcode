class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<(m*k):
            return -1
        lo = 1
        hi = max(bloomDay)
        res = hi
        while lo <=hi:
            
            mid = lo + (hi-lo)//2

            if self.check(mid,bloomDay,m,k) and mid < res:
                res =mid
                hi = mid -1
            else:
                lo = mid + 1
        return res
    
    def check(self,mid,bloomDay,m,k):
        # check if m distict groups of k values in bloomDay are less than mid

        arr = [False]*(len(bloomDay))
        for i in range(len(bloomDay)):
            if bloomDay[i]<=mid:
                arr[i] = True
        
        left = 0
        count_groups = 0
        count_vals = 0
        for right in range(len(bloomDay)):
            if arr[right]==True:
                count_vals+=1
                if count_vals==k:
                    count_groups+=1
                    count_vals = 0
                    left = right
            else:
                left = right
                count_vals = 0
        
        return True if count_groups>=m else False
