class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        for i in range(len(min(strs))):
            c = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != c:
                    return res
            
            res += c
        
        return res
            