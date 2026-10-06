class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        t = [[float('inf')]*(amount+1) for _ in range(n+1)]
        for i in range(1,n+1):
            t[i][0] = 0
        for j in range(1,amount+1):
            if j%coins[0]==0:
                t[1][j] = j//coins[0]
        
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<= j:
                    t[i][j] = min(t[i][j-coins[i-1]]+1, t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]

        print(t[n][amount])    
        return t[n][amount] if t[n][amount] != float('inf') else -1