class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        t = [-1]*(n+1)
        t[0] = 0

        def houserob(n,nums):
            if n == 0:
                return 0
            if n == 1:
                return nums[n-1]
            if t[n-1]!=-1:
                return t[n-1]
            
            t[n-1] = max(nums[n-1]+houserob(n-2,nums),houserob(n-1,nums))
            return t[n-1]

        return houserob(n,nums)