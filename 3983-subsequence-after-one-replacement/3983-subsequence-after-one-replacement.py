class Solution(object):
    def canMakeSubsequence(self, s, t):
        n = len(s)
        i = 0
        j = 0

        for c in t:

            if j < n and c == s[j]:
                j += 1

            j = max(j, i + 1)

            if i < n and c == s[i]:
                i += 1

        return j >= n