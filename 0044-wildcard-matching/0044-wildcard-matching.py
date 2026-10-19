class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        t = [[False] * (m + 1) for _ in range(n + 1)]
        t[0][0] = True

        for j in range(1, m + 1):
            if p[j - 1] == '*':
                t[0][j] = t[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    t[i][j] = t[i][j - 1] or t[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    t[i][j] = t[i - 1][j - 1]

        return t[n][m]