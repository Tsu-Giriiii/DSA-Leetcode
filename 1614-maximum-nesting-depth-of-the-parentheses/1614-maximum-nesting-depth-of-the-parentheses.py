class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        arr = []
        for c in s:
            if c == '(':
                count+=1
            elif c==')':
                count-=1
            arr.append(count)
        return max(arr)