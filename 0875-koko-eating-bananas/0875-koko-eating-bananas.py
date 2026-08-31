class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo = 1
        hi = max(piles)
        k = hi

        while lo<=hi:
            mid = lo + (hi-lo)//2

            if self.check(mid,piles,h) and mid < k:
                k  = mid
                hi = mid -1

            
            else:
                lo = mid +1
        
        return k
    
    def check(self,mid,piles,h):
        count = 0
        for pile in piles:
            count += (pile+mid-1)//mid
        print(mid,count)
        if count <= h:
            return True
        return False