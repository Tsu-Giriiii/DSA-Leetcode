class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False]*(n+1) for _ in range(n+1)]      
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or pal[i+1][j-1]):
                    pal[i][j] = True
        
        t = [float('inf')]*(n+1)
        t[0] = 0

        for i in range(1,n+1):
            for j in range(i):
                if pal[j][i-1]:
                    t[i] = min(1+t[j],t[i]) 
        return t[n]-1