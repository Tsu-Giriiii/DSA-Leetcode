class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        S  = sum(nums)
        n = len(nums)

        if abs(target) > S or (S+target)%2!=0:
            return 0
        sub_target = S-(S+target)//2
        t = [[0]*(sub_target+1) for _ in range(n+1)]
        t[0][0]=1

        for i in range(1,n+1):
            for j in range(sub_target+1):
                
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][sub_target]
