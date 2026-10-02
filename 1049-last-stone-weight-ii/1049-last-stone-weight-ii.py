class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n = len(stones)
        S = sum(stones)

        t = [[False]*(S//2+1) for _ in range(n+1)]
        t[0][0] = True

        for i in range(1,n+1):
            for j in range(S//2+1):
                if stones[i-1]<=j:
                    t[i][j] = t[i-1][j-stones[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        mn = float('inf')
        arr = []
        arr[:] = t[n]
        for i in range(S//2+1):
            if arr[i] == True:
                mn = min(mn,S-2*i)
        return mn