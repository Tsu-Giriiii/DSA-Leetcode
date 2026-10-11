from collections import deque
class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        seen = set()

        for i in range(len(isConnected)):
            
            if i not in seen:
                seen.add(i)
                count+=1
                self.dfs(i,isConnected,seen)
        return count
        
    '''def bfs(self,u,isConnected,seen):
        q = deque([u])
        while q:
            t = q.popleft()
            for i in range(len(isConnected)):
                if i not in seen and isConnected[t][i]==1:
                    seen.add(i)
                    q.appendleft(i)'''
    
    def dfs(self,u,isConnected,seen):
        seen.add(u)
        for i,n in enumerate(isConnected[u]):
            if n == 1 and i not in seen:
                self.dfs(i, isConnected,seen)
        return seen
