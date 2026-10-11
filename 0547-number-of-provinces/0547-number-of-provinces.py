from collections import deque
class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        seen = set()

        for i in range(len(isConnected)):
            
            if i not in seen:
                seen.add(i)
                count+=1
                self.bfs(i,isConnected,seen)
        return count
        
    def bfs(self,u,isConnected,seen):
        q = deque([])
        q.append(u)
        while q:
            t = q.popleft()
            for i in range(len(isConnected)):
                if i not in seen and isConnected[t][i]==1:
                    seen.add(i)
                    q.appendleft(i)
