class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
            
            while count[s[right]]>2:
                count[s[left]]-=1
                left+=1
            longest = max(longest,right-left+1)
        
        return longest
