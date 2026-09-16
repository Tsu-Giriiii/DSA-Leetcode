class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = 1
        hi = max(nums)
        ans = float('inf')
        def div_sum(nums,div):
            result = 0
            for num in nums:
                result+= (num+div-1)//div
            return result

        while lo <= hi:
            mid = lo + (hi-lo)//2
            res = div_sum(nums,mid)
            print(res,mid)

            if res <= threshold and mid <= ans:
                    ans = mid
                    hi = mid - 1
            
            elif res > threshold:
                lo = mid+1
            
        
        
        return ans