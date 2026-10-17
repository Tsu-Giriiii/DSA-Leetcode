class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        t = [['']*(m+1) for _ in range(n+1)]

        

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = t[i-1][j-1]+str1[i-1]
                else:
                    t[i][j] = t[i-1][j] if (len(t[i-1][j]) > len(t[i][j-1])) else t[i][j-1]

        LCS = t[n][m]
        i = j = lcs_head = 0
        res = ''

        while lcs_head < len(LCS):

            while str1[i]!= LCS[lcs_head]:
                res += str1[i]
                i+=1
            
            while str2[j]!= LCS[lcs_head]:
                res+=str2[j]
                j+=1
            
            res += LCS[lcs_head]
            i+=1
            j+=1
            lcs_head+=1
        
        return res+str1[i:]+str2[j:]