class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        
        ans = 0
        for i in range(1,len(s)+1):
            prefix = s[:i]
            d = {'0':0,'1':0}
            for c in prefix:
                if c == '0':
                    d['0']+=1
                else:
                    d['1']+=1

            if abs(d['0']-d['1'])<=1:
                ans+=1
        return ans