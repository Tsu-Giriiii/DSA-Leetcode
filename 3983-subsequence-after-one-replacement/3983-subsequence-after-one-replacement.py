class Solution(object):
    def canMakeSubsequence(self, s, t):
        n = len(s)
        i = j = 0
        for c in t:
            j = max(j + (j < n and c == s[j]), i + 1)
            i += i < n and c == s[i]
        return j >= n