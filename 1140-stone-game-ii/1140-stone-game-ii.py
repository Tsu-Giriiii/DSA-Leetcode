class Solution:
    def stoneGameII(self, piles):
        #dp[i][m] max score difference alice can get from position i if M = m
        # we need to find dp[0][1], initially we can max to max 2 piles
        #dp[0][1] = max(piles[0]-dp[1][1]+piles[0]-dp[1][2]), piles[0]+piles[1](-dp[2][1],-dp[2][2],-dp[2][3],-dp[2][4])
        # so we need to start from rightmost element
        #dp[n-1][m] = piles[n] for all values of m because only 1 element can be fetched
        #dp[n-2][m] = we two options take 1 or take 2
        #             max(piles[n-2]-dp[n-1][1],(piles[n-2]+piles[n-1])-dp[n-1][2])
        #So that gives the recurrence as follows
        # score_difference = current_pile - min(opponent_sd)
        #dp[i][m] = max()
        
        
        n = len(piles)

        # suffix[i] = total stones from i to n-1
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones current player can collect
        # starting from index i with current M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Base case:
        # If i == n, there are no piles left -> 0 stones

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # If we can take all remaining piles
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                for X in range(1, 2 * M + 1):
                    new_M = max(M, X)

                    # Stones we take
                    taken = suffix[i] - suffix[i + X]

                    # Opponent gets the optimal result from there
                    opponent = dp[i + X][new_M]

                    # Remaining stones after opponent's optimal play
                    current = suffix[i] - opponent

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]
