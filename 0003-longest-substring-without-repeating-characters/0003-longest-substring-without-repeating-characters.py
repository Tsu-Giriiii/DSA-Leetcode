class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="":
            return 0

        left = 0
        right = 0
        visited = set()
        res = 0
        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
                right+=1
                res = max(res,right-left)

            else:
                
                while s[right] in visited:
                    visited.remove(s[left])
                    left +=1
            
        return res

        