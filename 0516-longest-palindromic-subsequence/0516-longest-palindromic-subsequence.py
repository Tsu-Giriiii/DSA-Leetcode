class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        rev_s = s[::-1]

        t = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rev_s[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        
        return t[n][n]